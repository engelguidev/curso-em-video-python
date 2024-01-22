print('-'*30)
print('{:^30}'.format('GAME ON!'))
print('{:^30}'.format('PEDRA, PAPEL OU TESOURA'))
print('-'*30)
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0,2)
print('Suas opções:')
print('[0] - PEDRA')
print('[1] - PAPEL')
print('[2] - TESOURA')
escolha = int(input('Qual é a sua escolha? '))
from time import sleep
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('-'*30)
print('Computador jogou {}'.format(itens[bot]))
sleep(1)
print('O jogador jogou {}'.format(itens[escolha]))
sleep(0.5)
print('-'*30)
sleep(1)
if bot == 0: #Jogou Pedra
    if escolha == 0:
        print('Ambos jogaram Pedra, empate!')
    elif escolha == 1:
        print('Papel ganha de Pedra, jogador venceu!')
    elif escolha == 2:
        print('Pedra ganha de Tesoura, jogador perdeu!')
    else:
        print('Opção inválida')
elif bot == 1: #Jogou Papel
    if escolha == 0:
        print('Papel ganha de Pedra, jogador perdeu!')
    elif escolha == 1:
        print('Ambos jogaram Papel, empate!')
    elif escolha == 2:
        print('Tesoura ganha de Papel, jogador venceu!')
    else:
        print('Opção inválida')
elif bot == 2: #Jogou Tesoura
    if escolha == 0:
        print('Pedra ganha de Tesoura, jogador venceu!')
    elif escolha == 1:
        print('Tesoura ganha de Papel, jogador perdeu!')
    elif escolha == 2:
        print('Ambos jogaram Tesoura, empate!')
    else:
        print('Opção inválida')
sleep(2)
print('O programa encerrará automaticamente')
sleep(7)