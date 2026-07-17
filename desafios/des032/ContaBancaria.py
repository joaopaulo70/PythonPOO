from pwinput import pwinput
import hashlib

class ContaBancaria:
    """
    Cria uma  conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome=None, saldo=0, chave=None):
        self._id = int(id)
        self._titular = nome
        self.__saldo = saldo
        if chave == None:
            chave = self.pede_senha()
            self.__hash = chave
        else:
            cript = hashlib.sha256(chave.encode())
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

    def pede_senha(self):
        senha = str(pwinput(prompt='Senha: ', mask='*'))
        senha_hash = hashlib.sha256(senha.encode())
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


