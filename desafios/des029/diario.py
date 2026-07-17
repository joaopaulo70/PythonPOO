from rich import print

class Diario:
    def __init__(self, senhamestra='CeV!@'):
        self.__segredos = []
        self.__senha = senhamestra.strip()
        self.senha = PermissionError('Ninguém pode ver a senha')
    
    @property
    def senha(self):
        raise PermissionError('Ninguém pode ver a senha')
    
    @senha.setter
    def senha(self, senha):
        pass

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())
    
    def ler(self, senha=None):
        if senha == self.__senha:
            print('[green]Diário LIBERADO![/]')
            for item in self.__segredos:
                print(f'- {item}')
        else:
            raise PermissionError('Senha inválida! Você não pode ler meu diário!')

