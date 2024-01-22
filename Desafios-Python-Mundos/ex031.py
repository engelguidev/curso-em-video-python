print('--- ENGELS TURISMO - CÁLCULO DE VIAGEM ---')
km = float(input('Digite quantos KM são até o destino: '))
ateduz = (km * 0.50)
maisduz = (km * 0.45)
print('CALCULANDO..')
if km <= 200.00:
    print('Sua viagem não ultrapassa 200 KM, então o custo é de R$ 0,50 por KM, totalizando R$ {:.2f}'.format(ateduz))
else:
    print('Sua viagem ultrapassa 200 KM, então o custo é de R$ 0,45 por KM, totalizando R$ {:.2f}'.format(maisduz))
