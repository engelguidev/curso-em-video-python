val = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in val:
        val.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não será adicionado.')
    r = str(input('Quer continuar? [S/N]: '.strip()))
    if r in 'Nn':
        break
val.sort()
print(f'Você digitou os valores {val}')
