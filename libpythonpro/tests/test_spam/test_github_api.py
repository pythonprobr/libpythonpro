import unittest.mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = unittest.mock.Mock()
    url = 'https://avatars.githubusercontent.com/u/62628200?v=4'
    resp_mock.json.return_value = {
        'login': 'Rawston', 'id': 62628200,
        'avatar_url': url,
    }
    # Salvamento do get original
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


# Sem acesso a rede
def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Rawston')
    assert 'https://avatars.githubusercontent.com/u/62628200?v=4' == url


# Com acesso a rede
def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Rawston')
    assert 'https://avatars.githubusercontent.com/u/62628200?v=4' == url
