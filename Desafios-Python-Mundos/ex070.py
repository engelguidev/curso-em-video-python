totgasto = 0
maisdemil = 0
menor = 0
cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = int(input('Valor do protudo: R$ '))
    cont += 1
    maisbarato = ' '
    totgasto += valor
    if valor > 1000:
        maisdemil += 1
    if cont == 1:
        menor = valor
        barato = produto
#também posso fazer esse trecho assim:
  #if cont == 1 or valor < menor:
        #menor = valor
        #barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto foi R$ {totgasto:.2f}.')
print(f'Foram {maisdemil} produtos acima de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} e custa {menor:.2f}')