from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, num_pag):
        self.titulo = titulo
        self.num_pag = num_pag
        self.pag_atual = 1
        print(f":book: [blue]Você acabou de abrir o livro [red]'{titulo}'[/] que tem [green]{num_pag} páginas[/] no total. \nVocê agora está na [yellow]página {self.pag_atual}[/]")

    def avancar_paginas(self, num=1):
        avancou = 0
        for pag in range(0, num):
            if not self.fim_do_livro():
                self.pag_atual += 1
                avancou += 1
                print(f'Pág{self.pag_atual} :arrow_forward: ', end='')
                sleep(0.2)
        print(f'[blue] Você avançou {avancou} páginas e agora está na [yellow]página {self.pag_atual}[/]')
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self):
         return True if self.pag_atual == self.num_pag else False



l1 = Livro('10 coisas que aprendi', 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
l1.avancar_paginas(5)