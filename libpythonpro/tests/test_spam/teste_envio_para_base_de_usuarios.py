from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.t_enviador_email import Enviador
from libpythonpro.tests.test_spam.conftest import sessao


def test_envio_de_spam(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'jnnbrag@gmail.com',
        'Curso Python Pro',
        'Excelentes Modulos'
    )

@pytest.mark.parametrize(

    'usuarios',
    [
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br'),
              Usuario(nome='Luciano', email='renzo@python.pro.br')
        ]
        [
            Usuario(nome='Renzo', email='renzo@python.pro.br')
        ]
    ]
)
def test_qde_envio_spam(sessao):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jnnbrag@gmail.com',
        'Curso Python Pro',
        'Excelentes Modulos'
    )


    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto,corpo)
        self.qtd_email_enviador +=1


def test_parametros_de_spam():
    for usuario in usuarios:
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
