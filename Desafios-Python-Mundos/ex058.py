'''from random import choice
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
    print('Errou rudeeeee')'''
from random import randint
computador = randint(0, 3)
print('Sou o seu computador, acabei de pensar em um número entre 0 e 10..')
print('Consegue adivinhar qual é?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Um pouco mais.. tente novamente')
        elif jogador > computador:
            print('Um pouco menos.. tente novamente')
print('Acertou com {} palpites, parabéns otário!'.format(palpites))

