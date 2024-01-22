import math
n = float(input('Digite o valor para um angulo: '))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print('O ângulo de {:.2f}, tem:\nO seno de {:.2f}.\nO cosseno de {:.2f}.\nA tangen de {:.2f}.'.format(n, sen, cos, tan))
#Posso fazer também
#from math import radians, sin, cos, tan
#após digitar acima, só remover os math
