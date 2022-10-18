import pytest

from Libpythonpro.spam.test_spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br','renzo@python.pro.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatario
    resultado = enviador.enviar(
        destinatario,
        'luciano@python.pro.br',
        'Cursos Python Pro',
        'Primeira Turma Guido Von Rossum aberta.')
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','renzo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciano@python.pro.br',
            'Cursos Python Pro',
            'Primeira Turma Guido Von Rossum aberta.'
        )

