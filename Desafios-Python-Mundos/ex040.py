print('-'*40)
print('         CALCULADOR DE MÉDIA')
print('-'*40)
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
if media < 5.0:
    print('Aluno com média de {}, reprovado por falta de nota'.format(media))
elif media >= 5.0 and media < 6.9:
    print('Aluno com média de {}, em recuperação'.format(media))
else:
    print('Aluno com média de {}, aprovado, meus parabéns'.format(media))
