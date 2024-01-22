t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
decimo = t + (10 - 1) * r
for n in range(t, decimo + r, r):
    print(n)
print('Fim')
