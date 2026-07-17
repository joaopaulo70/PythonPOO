# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um  gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use:
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome='<desconhecido>', idade=0): # Método Construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'
    
    def __getstate__(self): # Dunder Method
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de Objetos
g1 = Gafanhoto('João Paulo', 17)
g1.aniversario()
# print(g1)
print(g1.__dict__) #  Dunder Attribute
print(g1.__getstate__()) # Dunder Method
print(g1.__class__) # Dunder Attribute

# print(g1.__doc__) # Dunder Attribute