lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 10.90,
         'Estojo', 8.99,
         'Compasso', 15,
         'Mochila', 160,
         'Caneta', 6.50,
         'Livro', 34.99)
print('-'*41)
print(f'{"LISTA DE PREÇOS":^41}')
print('-'*41)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R$ {lista[pos]:>7.2f}')