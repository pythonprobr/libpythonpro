import pytest

from ...spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['99@rara.com.br', 'doougals.@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado=enviador.enviar(
        remetente,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Prieiira turma Guido Von Rossum aberta.'
    )

    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'doougals.ail.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Cursos Python Pro',
            'Prieiira turma Guido Von Rossum aberta.'
        )