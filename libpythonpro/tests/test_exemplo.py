import pytest
from libpythonpro.github_api import buscar_avatar, buscar_nome


@pytest.mark.parametrize(
    'usuario',
    ['avellar1975', 'renzo']
)
def test_buscar_avatar(usuario):
    resultado = buscar_avatar(usuario)
    assert resultado is not None


def test_buscar_nome():
    resultado = buscar_nome('avellar1975')
    assert resultado is not None
