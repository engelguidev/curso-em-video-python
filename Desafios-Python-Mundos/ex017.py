'''from math import sqrt, pow
catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))
c = pow(catop, 2)+pow(catad, 2)
hip = sqrt(c)
print('O triângulo com o cateto oposto de {} e o cateto adjacente com {}, resulta na hipotenusa de: {}'.format(catop, catad, hip))'''
#Meu exercício feito acima, abaixo como o professor fez
#import math
#ou
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(co, ca)
print('O triangulo com o cateto oposto {} e o cateto adjacente {}, resulta numa hipotenusa de {:.2f}'.format(co, ca, hip))
