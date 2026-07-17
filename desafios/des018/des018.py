from rich.panel import Panel
from rich import print
from rich.traceback import install

install()

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
    
    def analisar(self):
        carne = self.quant * 0.4
        tot = carne * 82.40
        pagar = tot / self.quant
        conteudo = f'Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n'
        conteudo += f'Cada participante comerá 0.4kg e cada Kg custa R$82.40\n'
        conteudo += f'Recomendo [blue]comprar {carne:.2f}kg[/] de carne\n'
        conteudo += f'O custo total será de [green]R${tot:,.2f}[/]\n'
        conteudo += f'Cada pessoa pagará [yellow]R${pagar:,.2f}[/] para participar.'
        painel = Panel(conteudo, title=self.titulo, )
        print(painel)

c1 = Churrasco('Churras dos amigos', 15)
c1.analisar()

c2 = Churrasco('Festa do fim de ano', 80)
c2.analisar()
