from credencial import *
from rich import inspect

def main():
    c = Credencial()
    c.senha = str(input('Digite a sua senha: '))
    print(c.senha)

    c.validar('Guanabara')

if __name__ == '__main__':
    main()
