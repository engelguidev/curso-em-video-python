print('-'*50)
print('              ALISTAMENTO MILITAR')
print('-'*50)
nome = str(input('Informe o seu nome: '))
ano = int(input('Informe o ano de nascimento: '))
from datetime import date
idade = (ano - date.today().year)*(-1)
difmenor = (idade - 18)*(-1)
difmaior = (idade - 18)
#print(difmenor)
#print(idade)
if idade < 18:
    print('Você têm {} anos, ainda não é hora de se alistar, logo será, restam {} anos para se alistar.'.format(idade ,difmenor))
elif idade == 18:
    print('Você têm {} anos, está na hora de se alistar.'.format(idade))
else:
    print('Você têm {} anos, já se passou {} anos do seu alistamento, seu merda.'.format(idade, difmaior))
