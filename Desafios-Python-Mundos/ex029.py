print('-- VELOCIDADE DE UM CARRO --')
vel = float(input('Qual é a velocidade do carro? '))
mult = (vel - 80)*7
if vel >= 81.00:
    print('Você foi multado! Cada KM é cobrado R$ 7,00. Você irá pagar R$ {:.2f}'.format(mult))
else:
    print('Você está dirigindo até o limite da velocidade, parabéns!')
