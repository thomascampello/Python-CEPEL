import os
import time
import math
from collections import Counter
#
Eliminar = """(
dbar:  56657  "OUROVE-RN034"    0.997475622854598    64.6146043872031     9   118
dbar:  56653  "BENTEVEOL034"    0.998879655801388    64.8169602492464     9   118
dbar:  56658  "OUROVE-RN138"    0.998189037315994    64.2700533781417     3   118
dbar:  56626  "JCMR3C-RN138"    0.997179471782352    64.0110284615037     3   118
dbar:  56671  "CATAND-RN138"     1.01088895729428    66.4857100711568     3   118
dbar:  56670  "CATAND-RN034"     1.00078282858437    70.9793574688439     9   118
dbar:  56668  "CATAN1EOL034"     1.00356477262519    71.3808699366563     9   118
dbar:  56669  "CATAN2EOL034"     1.00356477262519    71.3808699366563     9   118
(
dlin:  56653   56657    1   1              0.011732             0.029327             5.7e-005               1   0         0
dlin:  56658   56626    1   1              0.007087             0.037816             0.011135               1   0         0
dlin:  56671   56626    1   1              0.036348             0.088706             0.022656               1   0         0
dlin:  56668   56670    1   1              0.011732             0.029327             5.7e-005               1   0         0
dlin:  56669   56670    1   1              0.011732             0.029327             5.7e-005               1   0         0
(
dtr2:  56657 0.999321738252159                 0   56658                 1                 0                     0                   0.1                100    1   1        0
dtr2:  56657 0.999321738252159                 0   56658                 1                 0                     0                   0.1                100    2   1        0
dtr2:  56626 0.981499451336542                 0     523                 1                 0                     0                0.0289                100    1   1        0
dtr2:  56670  0.99358391686737                 0   56671                 1                 0                     0               0.33333                100    1   1        0
dtr2:  56670  0.99358391686737                 0   56671                 1                 0                     0               0.33333                100    2   1        0
(
deqp:  56653       0    1    1               4.515                  1.4                 0.06     p
deqp:    523       0    1    1                   0    0.666666666666667                    0     p
deqp:    523       0    2    1                   0    0.666666666666667                    0     p
deqp:  56668       0    1    1               4.515                  1.4                 0.06     p
deqp:  56669       0    1    1               4.515                  1.4                 0.06     p
deqp:    523       0    1    1 0.000333977884182791  0.00434985696012639                    0     s
("""
Eliminar_Linhas = Eliminar.splitlines()
#
pasta = os.path.dirname(os.path.abspath(__file__))
print('Pasta Atual: '+pasta)
arquivos_pasta = os.listdir(pasta)
arq_entrada = [arq for arq in arquivos_pasta if arq[-4:]=='.hzs']
print('Arquivos HZS que serão modificados: ')
print(arq_entrada)
n_casos= len(arq_entrada)
#
#
for caso in arq_entrada:
    arquivo_Hzs = str(open(pasta+'\\'+caso,'r+').read()).splitlines()
    arquivo_novo = caso[:-4]+'_Abordagem1.hzs'
    salvar = open(pasta+'\Resultado_Abordagem1'+'\\'+arquivo_novo,'w+')
    flag_lin = 0
    for linha in arquivo_Hzs:
        campos_lin = linha.split()
        for elim in Eliminar_Linhas:
            campos_elim = elim.split()
            if (campos_elim[0] == 'dmaq:'):
                if ( len(campos_elim)-1 == len(campos_lin) ):
                    if ( (campos_lin[0] == campos_elim[1]) & (campos_lin[1] == campos_elim[2] )):
                        flag_lin = 1
                        break
            elif (campos_elim[0] == 'deqp:'):
                if ( len(campos_elim)-1 == len(campos_lin) ):
                    if ( (campos_lin[0] == campos_elim[1]) & (campos_lin[1] == campos_elim[2] ) & 
                         (campos_lin[2] == campos_elim[3]) & (campos_lin[3] == campos_elim[4] ) ):
                        flag_lin = 1
                        break        
            elif (campos_elim[0] == 'dlin:'):
                if ( len(campos_elim)-1 == len(campos_lin) ):
                    if ( (campos_lin[0] == campos_elim[1]) & (campos_lin[1] == campos_elim[2] ) & 
                         (campos_lin[2] == campos_elim[3]) & (campos_lin[3] == campos_elim[4] ) ):
                        flag_lin = 1
                        break
            elif (campos_elim[0] == 'dtr2:'):
                if ( len(campos_elim)-1 == len(campos_lin) ):
                    if ( (campos_lin[0] == campos_elim[1]) & (campos_lin[3] == campos_elim[4] )):
                        flag_lin = 1
                        break
            elif (campos_elim[0] == 'dbar:'):
                if ( len(campos_elim)-1 == len(campos_lin) ):
                    if ( (campos_lin[0] == campos_elim[1]) & (campos_lin[1] == campos_elim[2] )):
                        flag_lin = 1
                        break
        if (flag_lin == 0):
            salvar.write('%s\n' %  linha)
        flag_lin = 0
    salvar.close()
                