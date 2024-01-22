def area(l, c):
    a = l * c
    print(f'A área entre a largura de {l} m e o comprimento de {c} m é de {a} m².')
from time import sleep


print('-='*20)
print('          CALCULADORA DE ÁREA')
print('-='*20)
l = float(input('Qual é a largura: '))
c = float(input('Qual é o comprimento: '))
print('Calculando..')
sleep(1)
area(l, c)