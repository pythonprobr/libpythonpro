import pytest
from libpythonpro.github_api import busca_avatar, busca_nome


@pytest.mark.parametrize(
    'usuario',
    ['avellar1975', 'renzo']
)
def test_busca_avatar(usuario):
    resultado = busca_avatar(usuario)
    assert resultado is not None


def test_busca_nome():
    resultado = busca_nome('avellar1975')
    assert resultado is not None
