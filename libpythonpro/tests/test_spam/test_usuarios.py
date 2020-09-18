from ...spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Douglas', email="doouglas@gmail.com.br")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Douglas', email="doouglas@gmail.com.br"),
        Usuario(nome='Dodo', email="doouglas@gmail.com.br")
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
