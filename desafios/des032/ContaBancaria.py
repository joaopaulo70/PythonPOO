from pwinput import pwinput
from hashlib import sha256

class ContaBancaria:
    """
    Cria uma  conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id:int, nome:str=None, saldo:float=0, chave:str=None):
        self._id = int(id) # protegido (#)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        if chave is None:
            chave = self.pede_senha()
            self.__hash = chave
        else:
            cript = sha256(chave.encode())
            key = cript.hexdigest()
            self.__hash = key
        print(f'Conta {id} criada com sucesso. Saldo atual de R${saldo:,.2f}')


    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, n):
        chave = self.pede_senha()
        if chave == self.__hash:
            self._titular = n

    def validar_senha(self, chave):
        if chave == self.__hash:
            return True
        else:
            return False

    def pede_senha(self) -> str:
        while True:
            senha = str(pwinput(prompt='Senha: ', mask='*'))
            if len(senha) >= 6:
                break
        senha_hash = sha256(senha.encode())
        return senha_hash.hexdigest()
    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self._id}')

    def sacar(self, valor, chave=None):
        if chave == None:
            chave = self.pede_senha()
        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque NEGADO de R${valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE.')
            else:
                self.__saldo -= valor
                print(f'Saque de R${valor:,.2f} autorizado na conta {self._id}')
        else:
            print('Senha não confere. Saque não autorizado!')


