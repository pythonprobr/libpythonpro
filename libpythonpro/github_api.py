# import requests
#
#
# def buscar_avatar(usuario):
#     """
#     Busca o avatar de um usuário no Github
#
#     :param usuario: str com o nome de usuário no github
#     :return: str com o link do avatar
#     """
#     url = f'https://api.github.com/users/{usuario}'
#     resp = requests.get(url)
#     return resp.json()['avatar_url']
#
#
# print(buscar_avatar('charlesnoamlael'))

import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuario no Github

    :param: usuario: str com o nome de usuario no git hub
    return: str com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


print(buscar_avatar('charlesnoamlael'))
