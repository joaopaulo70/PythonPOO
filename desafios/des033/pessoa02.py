from abc import ABC
from datetime import date
class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc
        
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} é inválido')

    @property
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    def idade(self, valor):
        raise PermissionError('Você não pode alterar a idade. Mude o ano de nascimento')

class Aluno(Pessoa):
    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc)
        self._curso = None
        self.curso = curso

    @property
    def curso(self):
        pass

    @curso.setter
    def curso(self, curso:str):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f'O Curso {curso} não se encontra na lista de cursos oficiais')

    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if 2 <= len(curso) <= 5 and curso not in Aluno.cursos_oficiais:
            Aluno.cursos_oficiais.append(curso)
        elif curso in Aluno.cursos_oficiais:
            raise ValueError(f'O Curso {curso} já está na lista de cursos oficiais')
        else:
            raise ValueError(f'Nome {curso} está fora do padrão para Cursos!')
