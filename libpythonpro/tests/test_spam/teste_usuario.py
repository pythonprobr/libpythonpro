class Sessao:
    contador = 0
    usuarios=[]

    def salvar(self, usuario):
        Sessao.contador +=1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    def listar(self):
        return self.listar()

class Conexao():
    def gerar_sessao(self)
        return Sessao()


class Usuario:
    def __init__(self,nome):
        pass


def test_salvar_usuario():
   conexao = Conexao()
   sessao = conexao.gerar_sessao()
   Usuario=Usuario(nome='Renzo')
   sessao.salvar(usuario)
   assert isinstance(usuario.id, int)
   sessao.roll_back()
   sessao.fechar()
   conexao.fechar()

def test_listar_usuarios():
   conexao = Conexao()
   sessao = conexao.gerar_sessao()
   Usuario=[Usuario(nome='Renzo'),Usuario(nome='Luciano')]
   for usuario in usuarios:
       sessao.salvar(usuario)
   assert usuario== sessao.listar()
   sessao.roll_back()
   sessao.fechar()
   conexao.fechar()