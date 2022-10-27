from menu import *
from equipamentos import *
from consult_opcao import *
from time import sleep
from sys import exit

while True:
    resposta = menu(['OLT','CTO','BAIRRO','CONDOMÍNIO','CLIENTE','SAIR'])
    if resposta == 1:
        print(linha())
        consulta_por_equipamento()
        sleep(1)
    elif resposta == 2:
        print(linha())
        consulta_cto()
        sleep(1)
    elif resposta == 3:
        print(linha())
        consulta_bairro()
        sleep(1)
    elif resposta == 4:
        print(linha())
        consultaCond()
        sleep(1)
    elif resposta == 5:
        print(linha())
        consulta_cliente()
        sleep(1)
    elif resposta == 6:
        print('-- Encerrando Aplicação -- ')
        print(linha())
        sleep(1)
        exit()

    else:
        print('[ERRO]! Digite uma opção válida!')
        sleep(1)

