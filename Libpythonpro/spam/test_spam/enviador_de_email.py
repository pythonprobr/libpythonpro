class Enviador:
    def __init__(self):
        self.qtd_email_enviados = 0

    def enviar(self, remetente, destinatário, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de Remetente Inválido:{remetente}')
        self.qtd_email_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
