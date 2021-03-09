import requests

def buscar_avatar(usuario):
    """
    Busca o avatar do github
    
    :param usuario: str com nome de usuario no github
    :return: str com link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


