print('-'*40)
print('         CATEGORIAS NADADORES')
print('-'*40)
from datetime import date
atual = date.today().year
nome = str(input('Nome do atleta: '))
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Calculando categoria do atleta..')
import time
time.sleep(2)
print('O atleta têm {} anos'.format(idade))
if idade <= 9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta Infantil')
elif idade <= 19:
    print('Atleta Junior')
elif idade <= 20:
    print('Atleta Sênior')
else:
    print('Atleta Master')



