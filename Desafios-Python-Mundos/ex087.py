matriz = [[0 , 0, 0], [0, 0, 0], [0, 0 , 0]]
par = ter = seg = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print(f'A soma dos valores pares --> {par}')
for l in range(0,3):
    ter += matriz[l][2]
print(f'A soma da terceira coluna --> {ter}')
for c in range(0,3):
    if c == 0:
        seg = matriz[1][c]
    elif matriz [1][c] > seg:
        seg = matriz[1][c]
print(f'O maior valor da segunda linha é --> {seg}')
