from uteis import numeros
num = int(input('Digite o preço: R$ '))
print(f'A metade de R$ {num} é R$ {numeros.metade(num)}')
print(f'O dobro de R$ {num} é R$ {numeros.dobro(num)}')
print(f'Aumentando 10%, temos {numeros.porcentopositivo(num, 10)}')