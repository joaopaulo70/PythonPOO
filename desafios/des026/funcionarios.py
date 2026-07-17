from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):

    sal_min = 1612
    inss = 0.925

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
    

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        self.minimos = self.salario / Funcionario.sal_min
        conteudo = f'O salário de [blue]{self.nome}[/] ([magenta]{type(self).__name__}[/]) é de '
        conteudo += f'[green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.minimos:.1f} salários mínimos[/].'
        painel = Panel(conteudo, title='Análise de Salário', width=49)
        print(painel)


class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab
    
    def calc_sal(self):
        self.salario = self.sal_bruto * Funcionario.inss


class FuncionarioMensalista(Funcionario):

    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto * Funcionario.inss
    
