from rich.panel import Panel
from rich import print
from rich.traceback import install
from rich.console import Console
from rich import inspect

console = Console()
install()

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        conteudo = f"{self.nome.center(30)}"
        conteudo += f"{'-' * 30}"
        preçof = f"R${self.preço:,.2f}"
        conteudo += f"{preçof.center(30, '.')}"
        print(Panel(conteudo, title='Produto', width=34))



p1 = Produto('Iphone 17 Pro Max', 25000.85)
p2 = Produto('Notebook Gamer', 8000)
p3 = Produto('Mouse', 125)
p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
