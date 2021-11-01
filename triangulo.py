'''Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo.
 Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo,
 calcular e escrever a área deste triângulo. Se não formam triângulo escrever os valores lidos.
 (Se a > b + c não formam triângulo algum, se a é o maior).'''

print ('-=' *20)
print ('ANALISADOR DE TRIANGULO')
print ('-=' *20)
####ENTRADA DE DADOS###
a = float(input('Digite o valor da base: '))
b = float(input('Digite a altura 1: '))
c = float(input('Digite a altura 2: '))

if(a < 0) or (b < 0) or (c < 0): #VERIFICA SE FOI DIGITADO ALGUM NUMERO NEGATIVO
   print ('-> DIGITES VALORES POSITIVOS !!!')

if (a + b < c) or (a + c < b) or (b + c < a):# VERIFICA SE É UM TRIANGULO
   print ('Os seguimento {}, {} e {}, NÃO FORMAM um triangulo'.format(a, b, c))
elif (a == b) and (a == c): #EQUILATERO
   area = (a * b) / 2
   print('Triangulo Equilatero e sua area é {}'.format(area))
elif(a == b) or (a == c) or (b == c):
   area = (a * b) / 2
   print('Triangulo Isosceles e sua area é {}'.format(area)) #ISOSCELES
else:
   area = (a * b) / 2
   print('Triangulo Escaleno e sua area é {}'.format(area)) #ESCALENO

