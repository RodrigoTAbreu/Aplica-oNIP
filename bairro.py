from PySimpleGUI import popup

def consulta_bairro():
    import sqlite3
    banco = sqlite3.connect('olt_banco.db')

    cursor = banco.cursor()
    #consulta = input("Informe o dado a ser consultado: ")
    #Realiza a pesquisa do banco apresentado todos os dados

    #bairro = input("Informe o bairro:").upper()
    popup('TESTE')

    print('Resultado: ')
    print('--'*40)

    cursor.execute(f"SELECT olt, pon, cto, nome, condominio, bairro FROM geral WHERE bairro='{bairro}'")

    for row in cursor:
        print(f'{row}'.replace(',','|').replace('(','').replace(')','').replace("'",""))
    print(cursor.fetchall())

consulta_bairro()