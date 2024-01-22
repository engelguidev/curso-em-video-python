print('-'*40)
print('{:^40}'.format('CONTAGEM REGRESSIVA'))
print('{:^40}'.format('ANO NOVO 2023'))
print('-'*40)
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('{:^40}'.format('FELIZ ANO NOVO!'))