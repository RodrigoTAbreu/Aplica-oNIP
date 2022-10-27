#CADASTRA EQUIPAMENTOS NO BANCO DE DADOS

import sqlite3
import os.path
resp = bool

banco = sqlite3.connect('olt_banco.db')

cursor = banco.cursor()

#Verefica se o Banco de dados já existe
res = os.path.exists('/Documentos/Curso Python/Python/Projeto-Gerando-Dados/consultaClientes/olt_banco.db')
 
if res is not True:
    #Cria a tabela
    cursor.execute("CREATE TABLE equipamentos (nome text, gpon text, cidade text)")

    #Insere Valores na Tabela
    nome = input("NOME DO EQUIPAMENTO: ")
    gpon = input("GPON: ")
    cidade = input("CIDADE: ")

    cursor.execute(f"INSERT INTO equipamentos VALUES('{nome}', '{cidade}')")
    #Salva ou atualiza o banco de dados
    banco.commit()
else:
    print("Banco de dados Já existe.")
