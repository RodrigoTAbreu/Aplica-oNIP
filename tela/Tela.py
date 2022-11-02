import PySimpleGUI as sg      
class TelaPython:
    def __init__(self):
        #Design da Tela
        sg.change_look_and_feel('DarkTeal6')
        #Janela de POPup
        sg.popup('Bem Vindo. Clique em OK para continuar.')
        #layout
        layout = [
            [sg.Text('Nome:', size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade:',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('GMail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Button('Enviar Dados')],       
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        
        
    def Iniciar(self):
        while True:
        #Extrair Dados da Tela
            self.button, self.values = self.janela.Read()
        
            '''print('Imprime de forma geral')
            print(self.values)
            print('--'*25)
            
            print('Imprime Dados Formatados')'''
            print('--'*30)
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            yahoo = self.values['yahoo']
            
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'GMail: {gmail}')
            print(f'Yahoo: {yahoo}')
            print(f'Outlook: {outlook}')   
              

tela = TelaPython()
tela.Iniciar()
        