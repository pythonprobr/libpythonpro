class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente invalido: {remetente} ')
        return remetente


class EmailInvalido(Exception):
    pass