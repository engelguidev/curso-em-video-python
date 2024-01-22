print('ANO BISSEXTO')
from datetime import date
ano = float(input('Digite um ano para saber se ele é bissexto, coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
quatro = (ano % 4)
quatrocen = (ano % 400)
cem = (ano % 100)
#print(quatro)
#print(quatrocen)
#print(cem)
if quatro == 0 and cem !=0 or quatrocen == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))