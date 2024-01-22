from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Maior
    [ 4 ] - Novos números
    [ 5 ] - Sair''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe novamente os números.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando..')
    else:
        print('Opção inválida! Digite novamente..')
    print('-'*30)
    sleep(1)
print('Fim do programa')
