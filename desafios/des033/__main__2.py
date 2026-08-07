from pessoa02 import *
from rich import inspect

def main():
    a1 = Aluno('João Paulo', 2009, 'ADM')
    a1.add_curso('TI')
    a2 = Aluno('Pedro', 2000, 'ENG')
    inspect(a2, methods=True, private=True)

if __name__ == '__main__':
    main()
