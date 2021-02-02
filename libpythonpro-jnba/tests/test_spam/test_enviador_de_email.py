class Enviador():
    def enviar(self, rementete, destinatrio, assunto, corpo):
        return 'jnbrag@gmail'



def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetnete():
    enviador = Enviador()
    resultado = enviador.enviar(
        'jnbrag@gmail.com',
        'gsealvarenga@gmail.com',
        'Curso Python Pro',
        'TDD e Baby Steps'
    )

    assert 'jnbrag@gmail' in resultado