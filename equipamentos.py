from menu import *
from consultas_nip import *
from time import sleep

def lista_do_equipamento():
    while True:
        resposta = menu(['OLT_HUAWEI_ALPHAVILLE_02', 'OLT_HUAWEI_CCP_01', 'OLT_HUAWEI_CCP_02', 'OLT_HUAWEI_CENTURY_1', 'OLT_HUAWEI_DOWNTOWN', 'OLT_HUAWEI_DOWNTOWN_00', 'OLT_HUAWEI_ELDORADO_01', 'OLT_HUAWEI_HELBOR_01', 'OLT_HUAWEI_HELBOR_02', 'OLT_HUAWEI_HELBOR_TTE_00', 'OLT_HUAWEI_JACAREI', 'OLT_HUAWEI_MANSAO', 'OLT_HW_PQTEC_01', 'OLT_HW_TREMEMBE', 'SAIR'])
        if resposta == 1:
            print(linha())
            print(menu[resposta])
            opc = 'OLT_HUAWEI_ALPHAVILLE_02'
            return opc
            sleep(1)
        elif resposta == 2:
            print(linha())
            opc = 'OLT_HUAWEI_CCP_01'
            return opc
            sleep(1)
        elif resposta == 3:
            print(linha())
            opc = 'OLT_HUAWEI_CCP_02'
            return opc
            sleep(1)
        elif resposta == 4:
            print(linha())
            opc = 'OLT_HUAWEI_CENTURY_1'
            return opc
            sleep(1)
        elif resposta == 5:
            print(linha())
            opc = 'OLT_HUAWEI_DOWNTOWN'
            return opc
            sleep(1)
        elif resposta == 6:
            print(linha())
            opc = 'OLT_HUAWEI_DOWNTOWN_00'
            return opc
            sleep(1)
        elif resposta == 7:
            print(linha())
            opc = 'OLT_HUAWEI_ELDORADO_01'
            return opc
            sleep(1)
        elif resposta == 8:
            print(linha())
            opc = 'OLT_HUAWEI_HELBOR_01'
            return opc
            sleep(1)
        elif resposta == 9:
            print(linha())
            opc = 'OLT_HUAWEI_HELBOR_02'
            return opc
            sleep(1)
        elif resposta == 10:
            print(linha())
            opc = 'OLT_HUAWEI_HELBOR_TTE_00'
            return opc
            sleep(1)    
        elif resposta == 11:
            print(linha())
            opc = 'OLT_HUAWEI_JACAREI'
            return opc
            sleep(1) 
        elif resposta == 12:
            print(linha())
            opc = 'OLT_HUAWEI_MANSAO'
            return opc
            sleep(1) 
        elif resposta == 13:
            print(linha())
            opc = 'OLT_HW_PQTEC_01'
            return opc
            sleep(1)      
        elif resposta == 14:
            print(linha())
            opc = 'OLT_HW_TREMEMBE'
            return opc
            sleep(1)      
        elif resposta == 15:
            print('Encerrando Consultas !!!')
            print(linha())
           # principal()
            break
        else:
            print('[ERRO]! Digite uma opção válida!')
            sleep(2)

