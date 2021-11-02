'''Faça um programa que leia 3 números inteiros e mostre o menor deles.'''

print('-=' *20)
print('TESTAR QUAL NUMERO DIGITADO É MENOR')
print('-=' *20)
####ENTRADA DE DADOS#####
nun1 = int(input('Digite o primeiro numero: '))
nun2 = int(input('Digite o segundo numero: '))
nun3 = int(input('Digite o terceiro numero: '))
menor = nun1 # MENOR RECEBE O PRIMEITO NUMERO DIGITADO
####TESTA QUAL NUMERO É MENOR####
if nun2 < menor:
    menor = nun2
if nun3 < menor:
    menor = nun3
print('O numero menor é {}'.format(menor)) #EXIBI QUAL NUMERO É O MENOR




