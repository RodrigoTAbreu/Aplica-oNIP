from time import sleep
import consultas_nip
from equipamentos import *
from sys import exit
#CONSULTA DO BANCO DE DADOS POR EQUIPAMENTOS E PON

def consulta_por_equipamento():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados
    opc = lista_do_equipamento()
    gpon = input("Informe a GPON: ")

    cont = 0
    print('Resultado: ')
    print('--'*40)
    cursor.execute(f"SELECT olt, pon, cto, nome FROM geral WHERE olt = '{opc}' AND pon = 'GPON {gpon}'")
    for row in cursor:
        cont += 1
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))

    if cont == 0:
        print('GPON NÃO LOCALIZADA PARA ESTA OLT >>')
        print('Iniciando Consulta por GPON')
        sleep(5)
        print('--'*20)
        cursor.execute(f"SELECT gpon, cto, codcliente, cliente FROM dados_cliente WHERE gpon = 'GPON {gpon}'")
        for row in cursor:
            print(f'{row}'.replace(',', '|').replace('(', '').replace(')', '').replace("'", ""))
        print(cursor.fetchall())

    

#CONSULTA DO BANCO DE DADOS POR CTO


def consulta_cto():
    import sqlite3 #importa a lib do sql
    banco = sqlite3.connect('olt_banco.db') #variavel se conecta ao bando de dados

    cursor = banco.cursor()

    #Realiza a pesquisa do banco apresentado todos os dados
    cto = input("Informe a CTO: ").upper()

    print('Resultado: ')
    print('--'*40)
    #Realiza a consulta com base na tabela GERAL apresentadno os dados somente desta tabela.
    #cursor.execute(f"SELECT olt, pon, cto, nome, condominio FROM geral WHERE cto = '{cto}'")
    #for row in cursor:
    #    print(row)

    #Realiza a pesquisa vinculando a consulta com duas tabelas distintas, com base na CTO que é campo em comum nas duas tabelas

    cont = 0
    cursor.execute(f"SELECT olt, pon, dados_cliente.CODCLIENTE, dados_cliente.CLIENTE FROM geral INNER JOIN dados_cliente on geral.cto = dados_cliente.cto WHERE geral.cto = '{cto}'")
    for row in cursor:
        cont += 1
        print(f'{cont: <2} - {row}'.replace(',','|').replace('(',' ').replace(')',' ').replace("'",""))

    print(cursor.fetchall())

    cursor.execute(f"SELECT olt, pon, cto, NOME, CONDOMINIO, ENDEREÇO, bairro FROM geral WHERE CTO='{cto}'")
    for row in cursor:
        cont += 1
        print(f'{cont: <2} - {row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))

    print(cursor.fetchall())

    if cont == 0:
        cursor.execute(f"SELECT gpon, cto, codcliente,  cliente FROM dados_cliente WHERE CTO='{cto}'")
        for row in cursor:
            print(f'Localizado Apenas->> CTO {row}'.replace(',', '|').replace('(', '').replace(')', '').replace("'", ""))
        print(cursor.fetchall())

#CONSULTA DO BANCO DE DADOS POR BAIRRO

def consulta_bairro():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")
    #Realiza a pesquisa do banco apresentado todos os dados

    bairro = input("Informe o bairro:").upper()

    print('Resultado: ')
    print('--'*40)

    cursor.execute(f"SELECT olt, pon, cto, nome, condominio, bairro FROM geral WHERE bairro='{bairro}'")

    for row in cursor:
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))
    print(cursor.fetchall())


#CONSULTA DO BANCO DE DADOS POR CONDOMINIO

def consultaCond():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados

    cond = input("Informe o condomínio:").upper()

    print('Resultado: ')
    print('--'*40)
    cursor.execute(f"SELECT olt, pon, codigo, circuito, nome FROM geral WHERE condominio='{cond}'")
    for row in cursor:
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))
    print(cursor.fetchall())
    
#CONSULTA POR CÓDIGO DE CLIENTE
def consulta_cliente():
    import sqlite3 #importa a lib do sql
    banco = sqlite3.connect('olt_banco.db') #variavel se conecta ao bando de dados

    cursor = banco.cursor()

    #Realiza a pesquisa do banco apresentado todos os dados

    cliente = input("Informe o C do Cliente:").upper()

    print('Resultado: ')
    print('--'*40)
    #Realiza a consulta com base na tabela GERAL apresentadno os dados somente desta tabela.
    #cursor.execute(f"SELECT olt, pon, cto, nome, condominio FROM geral WHERE cto = '{cto}'")
    #for row in cursor:
    #    print(row)

    #Realiza a pesquisa vinculando a consulta com duas tabelas distintas, com base na CTO que é campo em comum nas duas tabelas
    cursor.execute(f"SELECT cto, gpon, cliente  FROM dados_cliente WHERE CODCLIENTE='{cliente}'")
    for row in cursor:
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))
    print(cursor.fetchall())
    
    cursor.execute(f"SELECT olt, pon, CODIGO, CIRCUITO, NOME FROM geral WHERE CODIGO='{cliente}'")
    for row in cursor:
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))
    print(cursor.fetchall())
    
    
#Consulta por tipo de Cliente CORPORATIVO
def consulta_corporativo():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")

    #Realiza a pesquisa do banco apresentado todos os dados

    print("Clientes Corporativos: ")
    corp = 'CORPORATIVO'
    print('Resultado: ')
    print('--'*40)
    cursor.execute(f"SELECT olt, pon, cto, nome, condominio FROM geral WHERE TIPO = '{corp}'")
    for row in cursor:
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))
    print(cursor.fetchall())
    
# Lista os Equipamentos com base em uma lista de equipamentos  
def lista_do_equipamento():
    while True:
        resposta = menu(['OLT_HUAWEI_ALPHAVILLE_02', 'OLT_HUAWEI_CCP_01', 'OLT_HUAWEI_CCP_02', 'OLT_HUAWEI_CENTURY_1', 'OLT_HUAWEI_DOWNTOWN', 'OLT_HUAWEI_DOWNTOWN_00', 'OLT_HUAWEI_ELDORADO_01', 'OLT_HUAWEI_HELBOR_01', 'OLT_HUAWEI_HELBOR_02', 'OLT_HUAWEI_HELBOR_TTE_00', 'OLT_HUAWEI_JACAREI', 'OLT_HUAWEI_MANSAO', 'OLT_HW_PQTEC_01', 'OLT_HW_TREMEMBE', 'SAIR'])
        if resposta == 1:
            print(linha())
            print('OLT_HUAWEI_ALPHAVILLE_02')
            opc = 'OLT_HUAWEI_ALPHAVILLE_02'
            return opc
            sleep(1)
        elif resposta == 2:
            print(linha())
            print('OLT_HUAWEI_CCP_01')
            opc = 'OLT_HUAWEI_CCP_01'
            return opc
            sleep(1)
        elif resposta == 3:
            print(linha())
            print('OLT_HUAWEI_CCP_02')
            opc = 'OLT_HUAWEI_CCP_02'
            return opc
            sleep(1)
        elif resposta == 4:
            print(linha())
            print('OLT_HUAWEI_CENTURY_1')
            opc = 'OLT_HUAWEI_CENTURY_1'
            return opc
            sleep(1)
        elif resposta == 5:
            print(linha())
            print('OLT_HUAWEI_DOWNTOWN')
            opc = 'OLT_HUAWEI_DOWNTOWN'
            return opc
            sleep(1)
        elif resposta == 6:
            print(linha())
            print('OLT_HUAWEI_DOWNTOWN_00')
            opc = 'OLT_HUAWEI_DOWNTOWN_00'
            return opc
            sleep(1)
        elif resposta == 7:
            print(linha())
            print('OLT_HUAWEI_ELDORADO_01')
            opc = 'OLT_HUAWEI_ELDORADO_01'
            return opc
            sleep(1)
        elif resposta == 8:
            print(linha())
            print('OLT_HUAWEI_HELBOR_01')
            opc = 'OLT_HUAWEI_HELBOR_01'
            return opc
            sleep(1)
        elif resposta == 9:
            print(linha())
            print('OLT_HUAWEI_HELBOR_02')
            opc = 'OLT_HUAWEI_HELBOR_02'
            return opc
            sleep(1)
        elif resposta == 10:
            print(linha())
            print('OLT_HUAWEI_HELBOR_TTE_00')
            opc = 'OLT_HUAWEI_HELBOR_TTE_00'
            return opc
            sleep(1)    
        elif resposta == 11:
            print(linha())
            print('OLT_HUAWEI_JACAREI')
            opc = 'OLT_HUAWEI_JACAREI'
            return opc
            sleep(1) 
        elif resposta == 12:
            print(linha())
            print('OLT_HUAWEI_MANSAO')
            opc = 'OLT_HUAWEI_MANSAO'
            return opc
            sleep(1) 
        elif resposta == 13:
            print(linha())
            print('OLT_HW_PQTEC_01')
            opc = 'OLT_HW_PQTEC_01'
            return opc
            sleep(1)      
        elif resposta == 14:
            print(linha())
            print('OLT_HW_TREMEMBE')
            opc = 'OLT_HW_TREMEMBE'
            return opc
            sleep(1)      
        elif resposta == 15:
            print('-- Encerrando Aplicação -- ')
            print(linha())
            exit()
           # principal()
        else:
            print('[ERRO]! Digite uma opção válida!')
            sleep(1)

