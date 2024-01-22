from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['carteira'] = int(input('Carteiro de trabalho (0 para não tem): '))
if pessoa['carteira'] != 0:
    pessoa['contratacao'] = int(input('Ano da contratação: '))
    pessoa['salario'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.now().year)
print('-='*40)
for k, v in pessoa.items():
    print(f' {k} tem o valor {v}.')
