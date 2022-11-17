import xlrd
import sqlite3

#Abre o arquivo e a plnilha em excel
arq = xlrd.open_workbook_xls('dadosclientes.xls')
plan = arq.sheet_by_name('plan2')

#NOME recebe os dados da LINHA 1
nome = plan.row_values(1)

#NOME_CLIENTE recebe o valor na posição 1
nome_cliente = nome[1]

#conectando com o bco de dados
conn = sqlite3.connect('olt_banco.db')
cur = conn.cursor()

#insere dados no bco de dados
cur.execute(f'INSERT INTO dados_olt_clientes (pon, desc, equipamento) VALUES(0,{nome_cliente},teste)')

#faz a consulta e a exibe
cur.execute('SELECT desc FROM dados_olt_clientes')
for row in cur:
    print(row)
