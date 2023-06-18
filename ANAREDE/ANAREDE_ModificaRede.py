import os
import time

#-----Rotina para criar casos no ANAREDE-----#
start = time.time()
#Lista de Barras Candidatas
pasta = os.getcwd() #pasta atual
arquivos_pasta = os.listdir(pasta) #lista arquivos na pasta
arquivo_SAV = [arq for arq in arquivos_pasta if arq[-4:]=='.SAV'] #filtra arquivos SAV
n_arquivos = arquivo_SAV.__len__()
#-----Criar código ANAREDE para juntar casos-----#
str_repet = """ulog
2
->(nome_sav_lido) (2)
arqv rest
->(numero_Caso_restaurado) (4)
(ulog
(1
(Tabelador_SIN_RedeBasica.PWF
ulog
4
->(nome_relatorio) (10)
(
ulog
1
Deck.PWF
ulog
2
->(nome_sav_novo) (17)
arqv inic
sim
exlf newt crem qlim ctap cphs csca cpri ctaf stpo celo step TABE file
arqv grav novo areg jump
->(numero_cenário) (22)
("""


str_fim = """( FINALIZANDO
RELA RTAB FILE
ulog
4
FIM.TXT
FIM"""

print("Etapa 1 - cria arquivos PWF")

for n in range(0,n_arquivos):
    if ( n== 0 ):
        n_casos = 9
    else:
        n_casos = 6
    #codigo = open('principal.pwf','w')
    hist_atual = 'principal-'+str(arquivo_SAV[n])+'.pwf'
    salvar = open(hist_atual,'w+')
    # escreve parte do corpo do arquivo
    for i in range(1,n_casos+1):
        str_corpo = str_repet.splitlines()
        str_final = str_fim.splitlines()
        #
        cenario = str(i)
        str_corpo[2] = arquivo_SAV[n]
        str_corpo[4] = i
        str_corpo[10] = 'RELA_'+ str(arquivo_SAV[n]) + '_Caso_'+ str(i)+ '.DAT'
        str_corpo[17] = './resultados/' + arquivo_SAV[n][0:-4]+'_Modificado.SAV'
        if (i != 1):
            str_corpo[18] = '('
            str_corpo[19] = '('
        str_corpo[22] = i  

        salvar.write('(((((Inicio - Caso'+str(i)+'\n')
        for linhas in str_corpo:
            salvar.write('%s\n' % linhas)
        salvar.write('(((((FIM - Caso'+str(i)+'\n')
    #finaliza arquivo
    for linhas in str_final:
        salvar.write('%s\n' % linhas)
    salvar.close()
#
print("Etapa 2 - Executa PWF")
#Rodar os PWF para criar os SAV
arquivos_pasta = os.listdir(pasta)
nome_pwf = [arq for arq in arquivos_pasta if arq[:4]=='prin']
for pwf in nome_pwf:
    arquivo = pasta+'\\'+pwf
    print(arquivo)
    os.startfile(arquivo)
#    time.sleep(252)
    flag = 0
    while(1):
        arquivos2 = os.listdir(pasta)
        if flag == 1:
            break
        for arq in arquivos2:
            if arq=='FIM.TXT':
                os.system("taskkill /im ANAREDE.exe /f")
                time.sleep(3) # tempo para o anarede fechar
                os.remove('FIM.txt')
                os.remove('CPR_0001.SAV') 
                os.remove(arquivo)
                flag = 1
                break         
print("FIM")
end = time.time()
print(end - start)
#del arquivos_pasta, nome_pwf, pwf, arquivo
