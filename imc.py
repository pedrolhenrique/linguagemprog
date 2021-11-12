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
        imc = float(valores['peso']) / (float(valores['altura']) * 2)
        if imc < 17:
            print(' Nome: {}\n Endereço: {}\n IMC: {}\n Você esta muito abaixo do peso'.format(valores['nome'],
                                                                                               valores['endereço'], imc))
        elif (imc >= 17) and (imc <=18.49):
            print(' Nome: {}\n Endereço: {}\n IMC: {}\n Você esta abaixo do peso'.format(valores['nome'],
                                                                                         valores['endereço'], imc))
        elif (imc >= 18.50) and (imc <= 24.99):
            print(' Nome: {}\n Endereço: {}\n IMC: {}\n Peso normal'.format(valores['nome'],
                                                                                         valores['endereço'], imc))
        elif (imc >= 25) and (imc <= 29.99):
            print(' Nome: {}\n Endereço: {}\n IMC: {}\n Acima do peso'.format(valores['nome'],
                                                                            valores['endereço'], imc))
        elif (imc >= 30) and (imc <= 34.99):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Obesidade I'.format(valores['nome'],
                                                                            valores['endereço'], imc))
        elif (imc >= 35) and (imc <= 39.99):
            print(' Nome: {}\n Endereço: {}\n MMC: {}\n Obesidade II (severa)'.format(valores['nome'],
                                                                            valores['endereço'], imc))
        else:
            print(' Nome: {}\n Endereço: {}\n IMC: {}\n Obesidade III (mórbida)'.format(valores['nome'],
                                                                            valores['endereço'], imc))
    if eventos == 'Sair':
        break



