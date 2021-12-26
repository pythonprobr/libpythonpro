import pytest

from libpythonpro.spam.enviador_de_email import EmailInvalido, Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'houston_cam@msn.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'houston_cam@msn.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'Rawston']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'rawstonmpinto@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
