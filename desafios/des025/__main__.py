from transportes import *
from rich import print
from rich.table import Table
from rich import inspect

def main():
    dist = 80

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    tabela = Table(title='Tabela de Fretes')
    tabela.add_column('Distância')
    tabela.add_column('Tipo')
    tabela.add_column('Frete')
    
    for item in viagem:
        tabela.add_row(f'{dist}Km', f'{type(item).__name__}', f'{item.calc_frete()}')

    print(tabela)


if __name__ == '__main__':
    main()
