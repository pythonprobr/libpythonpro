from Libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario= Usuario(nome='Carlos', email= 'carhb@outlook.com' )
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Carlos', email='carhb@outlook.com'),
        Usuario(nome='Givani', email='carhb@outlook.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()



