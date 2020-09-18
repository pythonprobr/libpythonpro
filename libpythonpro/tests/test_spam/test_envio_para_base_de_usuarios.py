from unittest.mock import Mock

import pytest

from ...spam.enviador_de_email import Enviador
from ...spam.main import EnviadorDeSpam
from ...spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Douglas', email="doouglas@gmail.com.br"),
            Usuario(nome='Dodo', email="doouglas@gmail.com.br")
        ],
        [
            Usuario(nome='Douglas', email="doouglas@gmail.com.br"),
        ]
    ]
)
def test_envio_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
        enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'dodo@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Douglas', email="doouglas@gmail.com.br")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@gmail.com',
        "doouglas@gmail.com.br",
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )