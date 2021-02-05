import pytest

from libpythonpro.spam.t_enviador_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'jnbrag@gmail.com','gsealvarenga@gmail.com']

)

def test_remetente(destinatario):
    enviador = Enviador()
    resultado=enviador.enviar(
        destinatario,
        'gsealvarenga@gmail.com',
        'Curso Python Pro',
        'TDD e Baby Steps'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'jnbrag']

)

def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
        remetente,
        'gsealvarenga@gmail.com',
        'Curso Python Pro',
        'TDD e Baby Steps'
    )

