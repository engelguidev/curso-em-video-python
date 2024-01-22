#fibonacci --> o número anterior mais o atual = numero e assim por diante
termo = int(input('Digite quantos termos deseja do Fibonacci: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
t3 = t1 + t2
cont = 3
while cont <= termo:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim')
