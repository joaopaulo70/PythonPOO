from rich import print
from rich.panel import Panel

caixa = Panel(f'{'[bold blue]Esse aqui é um painel de exemplo[/]':^111}', title='A Morte de Cabo Daciolo', style='yellow', subtitle='Cabo Daciolo acaba de morrer na manhã dessa sexta-feira na cidade de Uruoca-CE')
print(caixa)
# print(Panel.__doc__)