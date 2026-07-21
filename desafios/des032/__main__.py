from ContaBancaria import *
from rich import print, inspect

def main():
    cc = ContaBancaria(000, 'Marcelo', 1000)
    cc.depositar(1000)

    cc.sacar(500)

if __name__ == '__main__':
    main()
