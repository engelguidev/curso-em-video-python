def fatorial(n = 0):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n = 0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)

def triplo(n = 0, formato=False):
    res = n * 3
    return res if formato is False else moeda(res)

def metade(n = 0, formato=False):
    res =  n / 2
    return res if formato is False else moeda(res)

def porcentopositivo(n = 0, taxa = 0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)

def porcentonegativo(n = 0 , taxa = 0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)

def moeda(preço = 0, moeda = 'R$ '):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('Resumo do Valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'A metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{porcentopositivo(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{porcentonegativo(preço, taxar, True)}')
    print('-'*30)