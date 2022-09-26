from Libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario= Usuario(nome='Carlos')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Carlos'), Usuario(nome='Givani')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



