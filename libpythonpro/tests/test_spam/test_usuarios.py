import pytest

from libpythonpro.spam.db import Conexao
from libpythonpro.spam.modelos import Usuario


@pytest.fixture(scope='session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Renzo'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
