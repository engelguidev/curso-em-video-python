'''cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')'''
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n #s=s+n
#print('A soma vale {}.'.format(s))
#Até que enfim o professor está falando sobre a atualização..
print(f'A soma vale{s}')