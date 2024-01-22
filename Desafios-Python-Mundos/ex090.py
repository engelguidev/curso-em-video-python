aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'Digite a média do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado.'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Em recuperação.'
else:
    aluno['situacao'] = 'Reprovado.'
for k, v in aluno.items():
    print(f' {k} é igual a {v}')
