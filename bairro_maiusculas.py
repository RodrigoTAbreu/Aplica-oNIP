#CONVERTE TODAS AS LETRAS PARA MAIUSCULAS

import sqlite3
banco = sqlite3.connect('olt_banco.db')

cursor = banco.cursor()


print('Resultado: ')
print('--'*40)

cursor.execute("UPDATE geral SET bairro = UPPER(bairro)")


print(cursor.fetchall())