'''val = []
val.append(5)
val.append(9)
val.append(4)
print(val)
val.sort(reverse=True)'''
'''val = list()
for cont in range (0, 5):
    val.append(int(input('Digite um valor: ')))
for c, v in enumerate (val):
    #print(f'{v}...', end='')
    print(f'Na posição {c}, encontrei o valor {v}.')'''
a = [1, 2, 3, 4, 5]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
