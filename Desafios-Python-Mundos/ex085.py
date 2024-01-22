lista = [[], []]
valores = 0
for c in range(1,8):
    valores = int(input(f'Digite o {c}º número: '))
    if valores % 2 ==0:
        lista[0].append(valores)
    else:
        lista[1].append(valores)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são: {lista[0]}')
print(f'Os valores ímpares são: {lista[1]}')
