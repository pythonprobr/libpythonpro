import requests


def avatar_seeker(user):
    """
    Seek for user's avatar in github

    :param user: users name in github
    :return: avatar image url
    """

    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(avatar_seeker('paulobueno'))
