import PySimpleGUI as sg 

sg.theme('SystemDefault')
"""
window = sg.Window(
    
    'CONSULTAS - NIP',
    size=(400,250),
    #element_justification = 'l', -->> Faz alinhamento dos itens de uma vez 'c' center, 'l' left, 'r' right
    
)"""
#Layout da coluna da Esquerda
layout_esquerda = [ 
    #[sg.Text("CONSULTAS NIP",key='titulo_tela', size=30)],
    [sg.Button('OLT',key='consulta_olt', size=15)], 
    [sg.Button('CTO', key='consulta_cto', size=15)],
    [sg.Button('BAIRRO', key='consulta_bairro', size=15)],
    [sg.Button('CLIENTE', key='consulta_cliente', size=15)],
    [sg.Button('CONDOMINIO',key='consult_cond', size=15)],
    [sg.Button('FINALIZAR', key='finaliza', size=15)],
              
]
#Layout da coluna da Direita
layout_direita = [
    [sg.Text('Consulta de Dados - NIP')]
]

#Layout que une as colunas
layout = [
    [sg.Column(layout_esquerda), sg.VSeparator(), sg.Column(layout_direita)]
]

#Carrega Janela
window = sg.Window(
    'App NIP', #titulo da janela
    layout = layout, 
)

window.read()

while True:
    evento, valores = window.read()
    
    if evento == sg.WIN_CLOSED:
        break

window.close()

"""
janela = sg.Window("APP - Consultas NIP", layout, size=(250,250))


while True:
    evento, valores = janela.read()
    
    if evento == sg.WIN_CLOSED:
        break"""