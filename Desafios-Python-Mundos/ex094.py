galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Comando inválido, digite novamente.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Opção inválida, tente novamente.')
    if resp == 'N':
        break
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('Foram cadastradas as seguintes mulheres: ',end='')
for c in galera:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ',end='')
print()
print('Lista de pessoas que estão com a idade acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ',end='')
        for k, v in p.items():
            print(f' {k} = {v}', end='')
        print()