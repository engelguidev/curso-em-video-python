from uteis import numeros
num = int(input('Digite o preço: R$ '))
print(f'A metade de {numeros.moeda(num)} é {numeros.metade(num, True)}')
print(f'O dobro de {numeros.moeda(num)} é {numeros.dobro(num, True)}')
print(f'Aumentando 10%, temos {numeros.porcentopositivo(num, 10, True)}')
print(f'Reduzindo 13%, temos {numeros.porcentonegativo(num, 13, True)}')