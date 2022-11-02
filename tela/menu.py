import PySimpleGUI as sg

sg.theme('Dark Blue 3')

layout = [
    [sg.Titlebar(title = 'CONSULTAS NIP')],
    [sg.Text('Escolha uma das opções')],
    [sg.OK('SAIR')]    
]

window = sg.Window('Escolha uma das Opções',layout)
event, values = window.read()

window.close()

