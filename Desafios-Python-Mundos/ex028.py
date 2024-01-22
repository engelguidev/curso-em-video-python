from random import choice
lista = [0, 1, 2, 3, 4, 5]
sort = choice(lista)
from time import sleep
#print(sort)
print('-- JOGO DA ADIVINHAÇÃO --')
print('--Tente adivinhar qual é o número que a máquina escolheu --')
print('Números de 0 a 5')
num = int(input('Adivinhe o número escolhido pela máquina: '))
print('Máquina diz: "Escolhendo o número.."')
sleep(3)
print('O número escolhido foi: {}'.format(sort))
if num == sort:
    print('Acertou mizeravi')
else:
    print('Errou rudeeeee')


