print('PROMOÇÃO - ENGELS IMPORTADORA')
print('Qualquer material com 5% de desconto!')
r=float(input('Qual o preço do produto desejado? R$ '))
d=r-(r*0.05)
print('O produto que custa R$ {:.2f} reais, na promoção está saindo R$ {:.2f} reais com 5% de desconto'.format(r, d))