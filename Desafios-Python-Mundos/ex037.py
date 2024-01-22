print('CONVERSOR DE NÚMEROS')
n = int(input('Digite um número: '))
print('[1] - Converter para Binário')
print('[2] - Converter para Octal')
print('[3] - Converter para Hexadecimal')
esco = int(input('Selecione uma opção: '))
from time import sleep
sleep(1)
if esco == 1:
    print('O número {} convertido para binário fica {}'.format(n, bin(n)[2:]))
elif esco == 2:
    print('O número {} convertido para octal fica {}'.format(n, oct(n)[2:]))
elif esco == 3:
    print('O número {} convertido para hexadecimal fica {}'.format(n, hex(n)[2:]))
else:
    print('Número inválido, tente novamente')
