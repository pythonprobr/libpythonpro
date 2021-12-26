from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Rawston', email='houston_cam@msn.com'),
            Usuario(nome='Marinho', email='rawstonmpinto@gmail.com')
        ],
        [
            Usuario(nome='Rawston', email='houston_cam@msn.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'houston_cam@msn.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Rawston', email='houston_cam@msn.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'rawstonmpinto@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'rawstonmpinto@gmail.com',
        'houston_cam@msn.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
