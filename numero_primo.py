'''Implementar uma função que retorne verdadeiro se o número for primo
(falso caso contrário). Testar de 1 a 100.'''
# Testa se o número é primo
def numprimo(n):

    if n < 2:
        return False

    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

for x in range(1, 101):###Vai de 1 ate 100###
    if numprimo(x):
        print (x)