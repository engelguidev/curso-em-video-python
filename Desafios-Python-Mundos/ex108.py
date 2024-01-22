from uteis import numeros
num = int(input('Digite o preço: R$ '))
print(f'A metade de {numeros.moeda(num)} é {numeros.moeda(numeros.metade(num))}')
print(f'O dobro de {numeros.moeda(num)} é {numeros.moeda(numeros.dobro(num))}')
print(f'Aumentando 10%, temos {numeros.moeda(numeros.porcentopositivo(num, 10))}')