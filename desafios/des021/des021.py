from rich import print
class Caneta:
    def __init__(self, cor='azul'):
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]'
            case 'verde':
                escolha = '[green]'
            case _:
                escolha = '[white]'
        self.cor = escolha
        self.tampar = True

    def destampar(self):
        self.tampar = False

    def quebrar_linha(self, linhas=1):
        print('\n' * linhas, end='')
    
    def escrever(self, texto):
        if not self.tampar:
            print(f'{self.cor}{texto}[/]', end=' ')
        else:
            print(f':prohibited: A {self.cor}caneta[/] está tampada!')

c1 = Caneta('Azul')
c2 = Caneta('vermelho')
c3 = Caneta('Verde')
c4 = Caneta('magenta')

c1.destampar()
c3.destampar()
c4.destampar()

c1.escrever('Olá, tudo bem?')
c1.quebrar_linha()
c2.escrever('Olá, Gafanhoto!')
c2.quebrar_linha()
c3.escrever('Vamos exercitar!')
c3.quebrar_linha()
c4.escrever('Eaí mano brother')
