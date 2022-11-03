import PySimpleGUI as sg
from cotacoes import pegar_catacoes

#Esse é o layout da tela de como vai ficar e seus elementos.
layout = [
    [sg.Text('Pegar Cotação da Moeda')], #Textp
    [sg.InputText(key="nome_cotacao")], #Input para entrada de dados
    [sg.Button('Pegar Cotação'),sg.Button('Cancelar')], #Botões
    [sg.Text("", key="texto_cotacao")] #Texto para apresentar o resultado.
]

janela = sg.Window("SISTEMA DE COTAÇÕES", layout)
#Nesse espaço vai todo o código dentro de While True
while True:
    evento, valores = janela.read()
    
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break

    if evento == 'Pegar Cotação':
        codigo_cotacao = valores["nome_cotacao"]
        cotacao = pegar_catacoes(codigo_cotacao) #chamando a função cotação e guardando em cotação.
        janela["texto_cotacao"].update(f"A cotação do {codigo_cotacao} é de R$ {cotacao}")

janela.close()
