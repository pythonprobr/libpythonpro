from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.t_enviador_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam= EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'jnnbrag@gmail.com',
        'Curso Python Pro'
        'Excelentes Modulos'
    )