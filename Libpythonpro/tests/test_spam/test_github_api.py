from unittest.mock import Mock

import pytest

from Libpythonpro import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/107650943?v=4'
    resp_mock.json.return_value = {
        'login': 'Carloshbfreire', 'id': 107650943,
        'avatar_url': url,
    }
    get_mock = mocker.patch('Libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Carloshbfreire')
    assert avatar_url == url

def test_buscar_avatar_integraçao():
    url = github_api.buscar_avatar('Carloshbfreire')
    assert 'https://avatars.githubusercontent.com/u/107650943?v=4' == url
