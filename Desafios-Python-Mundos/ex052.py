n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c))
print('\n\033[mO número {} foi dividido por {} vezes'.format(c, tot))
if tot == 2:
    print('O número {} é primo'.format(n))
else:
    print('O número {} não é primo'.format(n))
