from random import randint
print('-'*40)
print('{:^40}'.format('PAR OU ÍMPAR'))
print('-'*40)
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' ' #<-- atenção ao espaço entre os ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Você jogou {jogador} e o computador jogou {computador}..')
            print(f'Total : {total}')
            print('Você venceu!')
            v+= 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}..')
            print(f'Total : {total}')
            print(f'Você perdeu! Você venceu {v} vezes do computador.')
    elif tipo == 'I':
        if total % 2 ==0:
            print(f'Você jogou {jogador} e o computador jogou {computador}..')
            print(f'Total : {total}')
            print(f'Você perdeu! Você venceu {v} vezes do computador.')
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}..')
            print(f'Total : {total}')
            print('Você venceu!')
            v += 1
