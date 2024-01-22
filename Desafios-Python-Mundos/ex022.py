nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas:{}'.format(nome.upper()))
print('Seu nome em letras minúsculas:{}'.format(nome.lower()))
#div = nome.split()
print('Seu nome completo tem um total de: {} '.format(len(nome)-nome.count(' ')),'letras')
#print('Seu primeiro nome tem um total de: {} '.format(len(div[0])),'letras')
#Professor fez o último de forma diferente
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

