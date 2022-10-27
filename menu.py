def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('>> MENU <<')
    c = 1
    for item in lista:
        print(f'{c:2} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Opção:')
    return opc



cabecalho('-- CONSULTAS NIP V1.0 --')

