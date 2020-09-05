import pytest
from libpythonpro.github_api import busca_avatar


@pytest.mark.parametrize(
    'usuario',
    ['avellar1975', 'renzo']
)
def test_busca_avatar(usuario):
    resultado = busca_avatar(usuario)
    assert resultado is not None
