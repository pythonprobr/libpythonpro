"""API de consulta aos atributos de usuário no Github."""

import requests

def busca_avatar(usuario):
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(busca_avatar('avellar1975'))
