from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
    
    def add_favoritos(self, favorito):
        self.favoritos.append(favorito)
        self.favoritos.sort()
    
    def ficha(self):
        conteudo = f'Nome real: [black on blue]{self.nome}[/]\n'
        conteudo += f'Jogos favoritos:'
        for jogo in self.favoritos:
            conteudo += f'\n[blue]:video_game: {jogo}[/]'
        painel = Panel(conteudo, title=f'Jogador <{self.nick}>', width=40)
        print(painel)

j1 = Gamer('João Paulo Aguiar', 'Link_Polar')
j1.add_favoritos("One Shot")
j1.add_favoritos("Minecraft")
j1.add_favoritos("Final Fantasy VII")
j1.add_favoritos("Roblox")
j1.add_favoritos("The Legend of Zelda")
j1.ficha()

j2 = Gamer('Elison Dias', 'Yellow')
j2.add_favoritos("Roblox")
j2.add_favoritos("Minecraft")
j2.ficha()
