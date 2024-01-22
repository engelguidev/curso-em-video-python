print('-'*50)
print('         FINANCIE SUA CASA - SIMULE AQUI!')
print('-'*50)
casa = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual é o seu salário? R$ '))
anos = int(input('Quantos anos pretende financiar a casa? '))
prest = (casa)/(anos*12)
#print (prest)
#print(sal*0.30)
if prest <= (sal*0.30):
    print('Parabéns! Você consegue financiar sua casa, serão {} anos com R${:.2f} prestações mensais'.format(anos, prest))
elif prest > (sal*0.30):
    print('Infelizmente você não consegue financiar o imóvel no momento')