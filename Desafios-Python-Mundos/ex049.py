print('-'*20)
print('{:^20}'.format('TABUADA'))
print('-'*20)
n = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, n*c))