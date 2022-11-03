import PySimpleGUI as sg 

sg.theme('SystemDefault')

layout = [ 
          [sg.Text("CONSULTAS NIP",key='titulo_tela', size=30)],
          [sg.Button('OLT',key='consulta_olt', size=30)],
          [sg.Button('CTO', key='consulta_cto', size=30)],
          [sg.Button('BAIRRO', key='consulta_bairro', size=30)],
          [sg.Button('CLIENTE', key='consulta_cliente', size=30)],
          [sg.Button('CONDOMINIO',key='consult_cond', size=30)],
          [sg.Button('FINALIZAR', key='finaliza', size=30)]   
          ]

janela = sg.Window("APP - Consultas NIP", layout)


while True:
    evento, valores = janela.read()
    
    if evento == sg.WIN_CLOSED:
        break