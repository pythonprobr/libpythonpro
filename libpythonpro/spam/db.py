class Sessao:
    contador = 0
    usuarios=[]

    def salvar(self, usuario):
        Sessao.contador +=1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.listar()

    def roll_back(self):
        pass

    def fechar(self):
        pass


class Conexao():
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass