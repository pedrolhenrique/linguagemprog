from datetime import date
data = date.today()
data_atual = '{}/{}/{}'.format(data.day, data.month, data.year)
dia = int(input('digite o dia do seu nascimento: '))
mes = int(input('Digite do mes do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
sua_idade = data.year - ano
meses = sua_idade * 12
dias =  sua_idade * 365
print('Você tem {} anos, {} meses e {} dias '.format(sua_idade, meses, dias))

print('Consulta realizada na data ', data_atual)






