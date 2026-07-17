from diario import *
from rich import inspect

def main():
    d = Diario()
    d.escrever('Essa é primeira mensagem')
    d.escrever('estou aprendendo python')
    try:
        d.ler('CeV!@')
    except Exception as e:
        print(f'[red]ERRO: {e}[/]')
    #inspect(d, methods=True, private=True)


if __name__ == '__main__':
    main()
