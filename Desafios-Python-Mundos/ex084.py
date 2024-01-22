pessoas = list()
todos = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Digite um nome: ')))
    pessoas.append(float(input('Digite um peso: ')))
    if len(todos) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    resp = str(input('Quer continuar? [S/N]'))
    todos.append(pessoas[:])
    pessoas.clear()
    if resp in 'Nn':
        break
print(f'Os dados foram {todos}')
print(f'Você cadastrou {len(todos)} pessoas.')
print(f'O maior peso foi de {maior} Kg, do(a) ', end='')
for p in todos:
    if p[1] == maior:
        print(f'[{p[0]}]. ', end='')
print()
print(f'O menor peso foi de {menor} Kg, do(a) ', end='')
for p in todos:
    if p[1] == menor:
        print(f'[{p[0]}]. ', end='')
print()