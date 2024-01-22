print('-'*40)
print('          CALCULADORA DE IMC')
print('-'*40)
alt = float(input('Qual é a sua altura: '))
peso = int(input('Qual é o seu peso: '))
imc = (peso/alt**2)*10000
#print(imc)
if imc < 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f} e você está no seu peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f} e você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f} e você está com obesidade.'.format(imc))
else:
    print('Seu IMC é {:.2f} e você está com obesidade mórbida.'.format(imc))