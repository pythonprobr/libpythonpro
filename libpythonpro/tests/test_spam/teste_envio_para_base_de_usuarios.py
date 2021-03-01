from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario
from libpythonpro.spam.t_enviador_email import Enviador
from libpythonpro.tests.test_spam.conftest import sessao



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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jnnbrag@gmail.com',
        'Curso Python Pro',
        'Excelentes Modulos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jame', email='jnbrag@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
            'gsealvarenga@gmail.com',
            'Curso Python Pro',
            'Excelentes Modulos'
    )

    enviador.enviar.assert_called_once_with(
        'gsealvarenga@gmail.com',
        'jnbrag@gmail.com',
        'Curso Python Pro',
        'Excelentes Modulos'
    )
