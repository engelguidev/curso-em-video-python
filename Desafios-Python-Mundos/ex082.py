val = []
pares = []
impares = []
while True:
    val.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(val): #i é o indice, obrigatório.. v é o valor, que está em enumerate..
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitiados foram: {val}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')