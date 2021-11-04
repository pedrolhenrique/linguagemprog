"""Faça um programa que leia a idade de uma pessoa expressa em dias e
mostre-a expressa em anos, meses e dias."""


from datetime import date
data = date.today()
data_atual = '{}/{}/{}'.format(data.day, data.month, data.year)
idade = int(input('Digite sua idade em dias: '))
anos = idade / 365
meses = anos * 12

print('Você tem {} anos, {} meses e {} dias '.format(int(anos), int(meses), int(idade)))

print('Consulta realizada na data ', data_atual)






