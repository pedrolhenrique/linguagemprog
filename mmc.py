from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Nome do Paciente'),sg.Input(key='nome',size=(40,1))],
    [sg.Text('Endereço Completo'),sg.Input(key='endereço',size=(39,1))],
    [sg.Text('Altura (cm)'), sg.Input(key='altura', size=(20,1))],
    [sg.Text('Peso (Kg)'), sg.Input(key='peso',size=(20,1))],
    [sg.Button('Calcular'),sg.Button('Reiniciar'), sg.Button('Sair')],
]

janela = sg.Window('Tela de Login', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcular':
        mmc = float(valores['peso']) / (float(valores['altura']) * 2)
        if mmc < 17:
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Você esta muito abaixo do peso'.format(valores['nome'],
                                                                                               valores['endereço'], mmc))
        elif (mmc >= 17) and (mmc <=18.49):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Você esta abaixo do peso'.format(valores['nome'],
                                                                                         valores['endereço'], mmc))
        elif (mmc >= 18.50) and (mmc <= 24.99):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Peso normal'.format(valores['nome'],
                                                                                         valores['endereço'], mmc))
        elif (mmc >= 25) and (mmc <= 29.99):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Acima do peso'.format(valores['nome'],
                                                                            valores['endereço'], mmc))
        elif (mmc >= 30) and (mmc <= 34.99):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Obesidade I'.format(valores['nome'],
                                                                            valores['endereço'], mmc))
        elif (mmc >= 35) and (mmc <= 39.99):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Obesidade II (severa)'.format(valores['nome'],
                                                                            valores['endereço'], mmc))
        else:
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Obesidade III (mórbida)'.format(valores['nome'],
                                                                            valores['endereço'], mmc))


    if eventos == 'Sair':
        break



