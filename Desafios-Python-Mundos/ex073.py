times = ('Palmeiras', 'Corinthians', 'Atlético-MG',
         'Fluminense', 'Athletico-PR', 'Internacional',
         'Flamengo', 'Bragantino', 'Santos', 'São Paulo',
         'Ceará', 'Botafogo', 'Avaí', 'Goiás', 'Cuiabá',
         'Coritiba', 'América-MG', 'Atlético-GO', 'Fortaleza',
         'Juventude')
print (f'Lista de times do Brasileirão Série A 2022: {times}')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Fortaleza está na {times.index("Fortaleza")+1} posição')

