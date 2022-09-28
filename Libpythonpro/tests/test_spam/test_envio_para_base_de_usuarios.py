import pytest

from Libpythonpro.spam.main import EnviadorDeSpam
from Libpythonpro.spam.modelos import Usuario
from Libpythonpro.spam.test_spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatário, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatário, assunto, corpo)
        self.qtd_email_enviados += 1

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Carlos', email='carhb@outlook.com'),
            Usuario(nome='Givani', email='givanifcf@hotmail.com')
        ],
        [
            Usuario(nome='Carlos', email='carhb@outlook.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'carhb@outlook.com',
        'Curso Pythonpro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Carlos', email='carhb@outlook.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'givanifcf@hotmail.com',
        'Curso Pythonpro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio ==(
        'givanifcf@hotmail.com',
        'carhb@outlook.com',
        'Curso Pythonpro',
        'Confira os módulos fantásticos'
    )



