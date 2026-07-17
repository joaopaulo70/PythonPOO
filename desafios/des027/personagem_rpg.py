from rich import print
from abc import ABC, abstractmethod
from random import randint, choice
from rich.panel import Panel

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.vida_atual = vida
        self.golpe = []
    
    def atacar(self, alvo, força=100):
        if self.vida_atual > 0 and alvo.vida_atual > 0:
            self.alvo = alvo
            self.força = força
            ataque = f'[green]{self.nome}[/]([cyan]{self.vida_atual}[/]) atacou [red]{alvo.nome}[/]([cyan]{alvo.vida}[/])'
            ataque +=  f' com um [blue]{self.golpe}[/] de força [cyan]{self.força}[/]\n'
            dano = alvo.receber_dano(força)
            ataque += f'[blue]{alvo.nome}[/] recebeu [red]dano de {dano}[/]!'
            print(ataque)
        else:
            print(f'O ataque [green]{self.nome}[/] -> [red]{alvo.nome}[/] não pode acontecer')


    def receber_dano(self, força):
        damage = randint(1, força)
        self.vida_atual -= damage
        if self.vida_atual < 0:
            self.vida_atual = 0
        return damage

    @abstractmethod
    def curar(self):
        pass

    def status_jogo(self):
        conteudo = f'[blue]Nome[/]: {self.nome}\n'
        conteudo += f'[green]HP[/]: {self.vida_atual}/{self.vida}\n'
        conteudo += f'[orange3]Golpes[/]: {self.golpes}\n'
        conteudo += f'[red]Força[/]: {self.força}'
        painel = Panel(conteudo, title=f'{type(self).__name__}', width=35)
        print(painel)

class Guerreiro(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Pulo Giratório', 'Golpe de Machado']
        self.golpe = choice(self.golpes)


    def curar(self):
        cura_guerreiro = randint(0, 100)
        self.vida_atual += cura_guerreiro
        msg = f'[blue]{self.nome}[/] enrolou uma atadura nos ferimentos '
        msg += f'e [green]recuperou {cura_guerreiro} pontos[/] de vida.'
        print(msg)

class Mago(Personagem):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de Fogo', 'Tornado', 'Raio de luz']
        self.golpe = choice(self.golpes)
    
    def curar(self):
        cura_mago = randint(0, 100)
        self.vida_atual += cura_mago
        msg = f'[blue]{self.nome}[/] fez uma magia de cura '
        msg += f'e [green]recuperou {cura_mago} pontos[/] de vida.'
        print(msg)

