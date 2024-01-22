print('Gordo, o construtor, para saber quantos litros de tinta é necessário, favor preencher abaixo seu animal')
l=float(input('Qual é a largura da parede? '))
a=float(input('Qual é a altura da parede? '))
area=a*l
litro=area/2
print('A parede com {} m de largura e {} m de altura, totalizando {} m², assim, são necessários {} litros de tinta.'.format(l, a, area, litro))