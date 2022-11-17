import PySimpleGUI as sg 
#import bairro

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
    [sg.Button('OLT',key='-olt-', size=15)], 
    [sg.Button('CTO', key='-cto-', size=15)],
    [sg.Button('BAIRRO', key='-bairro-', size=15)],
    [sg.Button('CLIENTE', key='-cliente-', size=15)],
    [sg.Button('CONDOMINIO',key='-cond-', size=15)],
    [sg.Button('FINALIZAR', key='-finaliza-', size=15)],
              
]
#Layout da coluna da Direita
layout_direita_t = [
    [sg.Text('Consulta de Dados - NIP',key='-titres-')],
    [sg.Text(' ',key='-result-')],
    [sg.Menu([['Equipamentos-OLT', ['OLT_HELBOR-01','OLT_HELBOR-02','OLT_HELBOR-03']],['CTOs', ['Consulta - CTO', ]]])]
]

layout_direita_c = [
    [sg.Radio('OLT_HELBOR-01','OLT', default=False)],
    [sg.Radio('OLT_HELBOR-02','OLT')],
    [sg.Radio('OLT_HELBOR-03','OLT')],
    [sg.Radio('OLT_HELBOR-04','OLT')],

]
#Layout que une as colunas
layout = [
    [sg.Push()],#aplica um espaço
    [sg.Push()],
    [sg.Push()],
    [sg.Push()],
    [sg.Column(layout_esquerda), sg.VSeparator(), sg.Column(layout_direita_t)],
    
]

#Carrega Janela
window = sg.Window(
    'App -- NIP --', #titulo da janela
    size=(600,400),
    layout = layout, 
)

while True: #necessário para deixar a tela "rodando" o tempo todo.
    event, values =  window.read()    
    if event == sg.WIN_CLOSED or event == '-finaliza-':
        break
    if event == '-olt-':
        window['-titres-'].update('CONSULTA POR OLT')
        window['-titres-'].update('Teste')

    if event == '-cto-':
        window['-titres-'].update('CONSULTA POR CTO')
    if event == '-bairro-':
        window['-titres-'].update('CONSULTA POR BAIRRO')
        window['-result-'].update('RESULTADO 3')
    if event == '-cliente-':
        window['-titres-'].update('CONSULTA POR CLIENTE') 
        window['-result-'].update('Consulta Por Cliente')
    if event == '-cond-':
        window['-titres-'].update('CONSULTA POR CONDOMÍNIO')
        window['-result-'].update('RESULTADO 5')
   
    
    
window.close()
