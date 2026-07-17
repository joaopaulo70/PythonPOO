from ContaBancaria import *
from rich import print, inspect

def main():
    print('Criando a conta...')
    cc = ContaBancaria('123', 'João', 1000, 'Gafanhoto')

    print('Realizando depósito')
    cc.depositar(500)

    print('Realizando saque...')
    cc.sacar(200)

    print('Alterando nome do titular...')
    cc.nome = 'Manoel'

    inspect(cc, private=True, methods=True)

if __name__ == '__main__':
    main()
