"""def teste():
    x = 8
    print(f'na função teste, n vale {n}.')
    print(f'na função teste, x vale {x}')


#Programa principal
n = 2
print(f'No programa principal, x vale {x}')
teste()
print(f'No programa principal, n vale {n}')
#Resumindo.. o n é uma variável global e o x é uma variável local"""
"""def funcao():
    n1 = 4
    print(f'N1 local vale {n1}')
n1 = 2
funcao()
print(f'N1 global vale {n1}')"""
def somar(a=0, b=0, c=0): #Posso deixar assim, com os 0, para caso não tenho valor, assim não dá erro
    """Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Guilherme Engel"""
    s = a + b + c
    return s
r1 = somar(3 , 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}.')