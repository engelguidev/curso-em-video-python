jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    totpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, totpartidas):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*40)
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>}º ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Digite o número do jogador para mais detalhes: (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-='*40)
print('FIM')