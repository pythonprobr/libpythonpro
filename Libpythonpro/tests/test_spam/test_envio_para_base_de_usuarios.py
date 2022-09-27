import pytest

from Libpythonpro.spam.main import EnviadorDeSpam
from Libpythonpro.spam.modelos import Usuario
from Libpythonpro.spam.test_spam.enviador_de_email import Enviador

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Carlos', email='carhb@outlook.com'),
            Usuario(nome='Givani', email='carhb@outlook.com')
        ],
        [
            Usuario(nome='Carlos', email='carhb@outlook.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'carhb@outlook.com',
        'Curso Pythonpro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


