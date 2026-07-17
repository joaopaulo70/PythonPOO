from rich import print
from rich.tree import Tree
from rich.table import Table
from rich.traceback import install

install()
c = Tree('João Paulo', style='blue')
jovem = c.add('[red]Jovem[/]')
jovem.add('[orange3]Aspirante a Programador[/]')
jovem.add('[orange3]Estuda na escola Olímpio Sampaio da Silva[/]')
idade = c.add('[green]Idade: 17 anos[/]')
idade.add('[purple]Aniversário: 17/02/2009[/]')
maioridade = idade.add('[purple]Próximo ano completa 18 anos[/]')
maioridade.add('[cyan]Irá atingir a maioridade ano que vem[/]')
tabela = Table(title='Lista de desejos')
tabela.add_column('Produto', style='dark_blue')
tabela.add_column('Preço', style='red')
tabela.add_row('PC Gamer', 'R$5000,00')
tabela.add_row('Livro - Python POO', 'R$94,00')
print(c)
print()
print()
print(tabela)