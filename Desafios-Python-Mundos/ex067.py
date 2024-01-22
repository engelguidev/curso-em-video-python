n1 = 0
while True:
    print('-'*40)
    n1 = int(input('   Quer ver a tabuada de qual número? '))
    print('-'*40)
    if n1 < 0:
        print('Assim não po, somente números positivos.. programado encerrado..')
        break
    else:
        for i in range (1, 11):
            print(n1, ' x ', i, ' = ', n1*i)
