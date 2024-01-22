#Primeira forma de fazer:
print('\033[1;31mOlá, mundo\033[m')
#Segunda forma de fazer:
nome = str(input('Digite o seu nome: '))
print('Olá {}{}{}! Prazer em te conhecer!'.format('\033[4;34m', nome, '\033[m'))
