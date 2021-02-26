import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from libpythonpro.spam.t_enviador_email import Enviador
from libpythonpro.tests.test_spam.conftest import sessao

class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente,destinatario,assunto,corpo)
        self.qtd_email_enviados += 1

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jame', email='jnbrag@gmail.com.br'),
            Usuario(nome='Luciano', email='jnbrag@gmail.com.br')
        ],
        [
            Usuario(nome='Jame', email='jnbrag@gmail.com.br')
        ]
    ]
)





def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jnnbrag@gmail.com',
        'Curso Python Pro',
        'Excelentes Modulos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jame', email='jnbrag@gmail.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
            'gsealvarenga@gmail.com',
            'Curso Python Pro',
            'Excelentes Modulos'
    )

    assert enviador.parametros_de_envio == (
        'gsealvarenga@gmail.com',
        'jnbrag@gmail.com',
        'Curso Python Pro',
        'Excelentes Modulos'
    )
