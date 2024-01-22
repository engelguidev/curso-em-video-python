print('-'*40)
print('       VERIFICADOR DE TRIÂNGULOS')
print('-'*40)
r1 = float(input('Digite o primeiro número: '))
r2 = float(input('Digite o segundo número: '))
r3 = float(input('Digite o terceiro número: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('Esses números podem formar um triângulo')
else:
    print('Esses números não podem formar um triângulo')
