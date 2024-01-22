"""
Teste técnico dev Python Jr. para a empresa Voxus
Autor: Guilherme Engel Pereira
API utilizada: ChuckNorris.io (https://api.chucknorris.io)

"""

import requests
import json


def chuck_random():
    """
    Consome a API e retorna uma piada aleatória junto com um status code.

    """

    url = 'https://api.chucknorris.io/jokes/random'
    data = requests.get(url)
    busca = json.loads(data.text)

    print('Sua piada:', busca['value'])
    print(data)


def chuck_categoria():
    """
    Consome a API, informando quais categorias estão disponíveis,
    o usuário digita e categoria e retorna uma piada aleatória referente a categoria,
    caso não seja encontrada, será retornado um erro 404.

    """

    lista = ['animal', 'career', 'celebrity', 'dev',
             'explicit', 'fashion', 'food', 'history',
             'money', 'movie', 'music', 'political',
             'religion', 'science', 'sport', 'travel']
    print('Busca por categoria')
    print('Categorias disponíveis:', ', ' .join(lista))
    category = str(input('Digite a categoria: '))
    url = f'https://api.chucknorris.io/jokes/random?category={category}'
    data = requests.get(url)
    busca = json.loads(data.text)
    try:
        print(busca['value'])
    except KeyError:
        print('Categoria não encontrada - Error Code 404')


def chuck_query_limit():
    """
    Consome API retornando a palavra chave do operator e quantas piadas ele deseja,
    caso exista a piada, será retornado conforme a quantidade que pediu, caso não exista,
    será retornado o erro 404.

    """

    query = str(input('Digite o nome da busca: '))
    limit = int(input('Digite quantas piadas quer ver: '))
    url = f'https://api.chucknorris.io/jokes/search?query={query}'
    data = requests.get(url)
    try:
        for n in range(0, limit):
            busca = json.loads(data.text)['result'][n]['value']
            print(n+1, 'ª piada:', busca)
    except IndexError:
        print('Error Code 404')


#chuck_random()
#chuck_categoria()
#chuck_query_limit()