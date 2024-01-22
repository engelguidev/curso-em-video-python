'''from math import factorial
n = int(input('Digite um número para calcular o fatorial dele: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''
from time import sleep
c = int(input('Digite um número para calcular o fatorial dele: '))
f = 1
print('Calculando {}!...'.format(c))
sleep(2)
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
