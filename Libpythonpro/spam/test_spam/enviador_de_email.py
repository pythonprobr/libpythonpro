class Enviador:
    def enviar(self, remetente, destinatário, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de Remetente Inválido:{remetente}')
        return remetente


class EmailInvalido(Exception):
    pass
