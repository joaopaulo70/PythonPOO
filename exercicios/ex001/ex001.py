# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'
        
# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "João Paulo"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Elison"
g2.idade = 18
g2.aniversario()
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = "Godofredo"
g3.idade = 68
g3.aniversario()
print(g3.mensagem())
