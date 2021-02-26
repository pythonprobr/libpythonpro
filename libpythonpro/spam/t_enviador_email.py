class Enviador():
    set.qtd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetenteInvalido: {remetente}')
        self.qtd_email_enviado += 1
        return remetente


class EmailInvalido(Exception):
    pass