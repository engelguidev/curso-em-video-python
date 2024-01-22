'''filme = {'titulo':'Star Wars', 'ano':'1977', 'diretor':'George Lucas'}
print(filme.values())
print(filme.keys())
print(filme.items())
for k, v in filme.items():
	print(f'O {k} é {v}')'''
'''pessoas = {'nome':'Guilherme', 'sexo':'M', 'idade':'29'}
#print(f'O {pessoas["nome"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = '150'
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = []
estado = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado)
brasil.append(estado2)
print(brasil[0]['uf'])'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Digite o UF: '))
    estado['sigla'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
