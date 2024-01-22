primeiro = int(input('Digite um termo: '))
razao = int(input('Digite uma razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao #termo = termo + razao
    cont += 1
print('Fim')