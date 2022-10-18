import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github
    :Param usuário: str com o nome usuário no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


