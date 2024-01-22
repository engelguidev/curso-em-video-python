val = list()
while True:
    val.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Você digitou {len(val)} números.')
val.sort(reverse=True)
print(f'Os valores em ordem decrescente são {val}')
if 5 in val:
    print('O valor 5 foi encontrado na lista.')
else:
    print('O valor 5 não foi encontrado na lista.')