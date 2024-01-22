from time import sleep
print('-- AUMENTO SALARIAL --')
sleep(1)
print('Conforme normas da empresa, acima de R$ 1.250,00 o aumento será de 10%.\nE abaixo de R$ 1.250,00 o aumento será de R$ 15%.')
sleep(3)
nome = str(input('Informe o nome do funcionário: ')).strip()
sleep(1)
sal = float(input('Informe o salário do {}: '.format(nome)))
maior = sal + (sal*0.10)
menor = sal + (sal*0.15)
print('Calculando..')
sleep(4)
if sal > 1250:
    print('O salário do(a) {} foi atualizado em 10%, de R$ {:.2f}, foi para R$ {:.2f}'.format(nome, sal, maior))
else:
    print('O salário do(a) {} foi atualizado em 15%, de R$ {:.2f}, para R$ {:.2f}'.format(nome, sal, menor))
print('-- FIM DO CÁLCULO --')
