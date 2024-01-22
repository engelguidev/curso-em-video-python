'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite o último número: '))'''
#Professor fez parte igual a mim, vou fazer igual ao dele
numeros = (int(input('Digite um número: ')), int(input('Digite um número: ')),
           int(input('Digite um número: ')), int(input('Digite um número: ')), )
print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)}.')
if 3 in numeros:
    print(f'O primeiro valor 3 foi digitado na posição {numeros.index(3)}.')
else:
    print('O valor 3 não foi localizado')
for n in numeros:
    if n % 2 == 0:
        print(n, end='')