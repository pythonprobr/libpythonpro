from Libpythonpro.spam.main import EnviadorDeSpam
from Libpythonpro.spam.test_spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'carhb@outlook.com',
        'Curso Pythonpro',
        'Confira os módulos fantásticos'
    )
