class Enviador():
    def enviar (self, remetente, destinatario, assunto, corpo):
    pass


def teste_criar_enviador_de_email():
    enviador=Enviador()
    assert enviador is not None

def teste_remetente():
    enviador=Enviador()
    enviador.enviar('jnbrag@gmail.com','gsealvarenga@gmail.com','Turma 2020','Socorro')