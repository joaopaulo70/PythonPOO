from rich import print

class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # Atributo Protected (#)

    # Criando atributo validável
    @property
    def nota(self): #getter
        return self._nota
    
    @nota.setter
    def nota(self, valor): #setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('[red]Nota inválida[/]')
    
    @nota.deleter
    def nota(self):
        pass
