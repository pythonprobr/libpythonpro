from unittest.mock import Mock

from Libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'Carloshbfreire', 'id': 107650943,
        'avatar_url': 'https://avatars.githubusercontent.com/u/107650943?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('Carloshbfreire')
    assert 'https://avatars.githubusercontent.com/u/107650943?v=4' == url
