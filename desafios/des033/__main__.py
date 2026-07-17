from pessoa import *
from rich import print, inspect

def main():
    a1 = Aluno('Maria', 2000, 'ADS')

    a1.add_curso('MODA')
    a1.curso = 'MODA'
    a1.nascimento = 2010

    inspect(a1, private=True, methods=True)

if __name__ == '__main__':
    main()
