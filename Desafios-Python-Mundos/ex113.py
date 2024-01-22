def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro, favor digitar um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            n1 = float(input(msg))
        except (ValueError, TypeError):
            print('Erro, favor digitar um número inteiro válido')
            continue
        except KeyboardInterrupt:
            print('\nEntrada de dados interrompida pelo usuário')
            return 0
        else:
            return n1



#Programa Principal
n = leiaInt('Digite um número Inteiro: ')
r = leiaReal('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n} e o valor real foi {r}.')