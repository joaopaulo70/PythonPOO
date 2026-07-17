from hashlib import sha256
from rich import print

class Credencial:
    def __init__(self):
        self.__hash = None
    
    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave:str):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError('Senha inválida')

    def validar(self, chave:str):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('Senha Confere!')
            return True
        else:
            print('Senha não bate!')
            return False
        
