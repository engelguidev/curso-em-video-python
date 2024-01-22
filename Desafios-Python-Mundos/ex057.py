print('-'*30)
print('     CATÁLOGO DE BINÁRIES')
print('-'*30)
sexo = str(input('Qual é o seu sexo, ser binárie? [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, favor informar o sexo [M/F]: ')).strip().upper()[0]
print('Obrigado pela confirmação')

