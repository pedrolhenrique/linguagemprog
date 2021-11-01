"""Faça um programa que leia a idade de uma pessoa expressa
em dia,mes e ano e  mostra em anos meses e dia."""


from datetime import date
data = date.today()
data_atual = '{}/{}/{}'.format(data.day, data.month, data.year)
dia = int(input('digite o dia do seu nascimento: '))
mes = int(input('Digite do mes do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
sua_idade = data.year - ano #CALCULA OS ANOS#
meses = sua_idade * 12 #CALCULA OS MESES#
dias =  sua_idade * 365 #CALCULA OS DIAS#
print('Você tem {} anos, {} meses e {} dias '.format(sua_idade, meses, dias))

print('Consulta realizada na data ', data_atual)






