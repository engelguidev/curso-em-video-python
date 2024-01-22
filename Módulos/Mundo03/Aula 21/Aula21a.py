#Ajuda Interativa - Interactive Help
#help()

#Docstrings
def contador(i, f, p): #inicio, fim, passo
    #Docstring abaixo em verde.. dentro das """..."""
    """Faz uma contagem e mostra na tela
        :param i: = início
        :param f: = fim
        :param p: = passo"""
    c = i
    while c <= f:
        print(f'{c} ', end='..')
        c += p
    print('Fim')

contador(2, 10, 2)
help(contador)

"""def somar(a=0, b=0, c=0): #Posso deixar assim, com os 0, para caso não tenho valor, assim não dá erro
    """"""Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Guilherme Engel""""""
    s = a + b + c
    print(f'A soma vale {s}.')
somar(0, 2)
help(somar)"""

