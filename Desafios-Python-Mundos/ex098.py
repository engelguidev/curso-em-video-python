from time import sleep
def contador(i, f, p):
    if p < 0:
        p*= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contagem de {i} até o {f}, de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
            sleep(0.3)
        print('--> Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            cont -= p
            sleep(0.3)
        print('--> Fim')

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é sua vez de fazer a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
