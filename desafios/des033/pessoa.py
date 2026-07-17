from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int, curso:str):
        self._nome = nome
        self._nascimento = nasc
    
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, ano:int):
        if 1910 <= ano <= 2026:
            self._nascimento = ano
        else:
            raise ValueError(f'Ano {ano} é inválido')

    @property
    def idade(self):
        return date.today().year - self._nascimento
    
    @idade.setter
    def idade(self, idade):
        raise PermissionError('Você não pode alterar a idade. Mude o ano de nascimento')


class Aluno(Pessoa):
    def __init__(self, nome:str, nasc:int, curso:str):
        super().__init__(nome, nasc, curso)
        self.cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
        if curso not in self.cursos_oficiais:
            raise ValueError(f'O Curso {curso} não está na lista de cursos oficiais.')
        self._curso = curso
    
    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso:str):
        if novo_curso in self.cursos_oficiais:
            self._curso = novo_curso
        else:
            raise ValueError(f'O Curso {novo_curso} não está na lista de cursos oficiais.')

    def add_curso(self, curso:str):
        self.cursos_oficiais.append(curso)

    