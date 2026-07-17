from abc import ABC, abstractmethod
from rich import print
from math import pi

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass

    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.lado = lado
    
    def perimetro(self):
        return self.qtd_lados * self.lado
    
    def area(self):
        return self.lado ** 2

class Circulo(Poligono):
    def __init__(self, raio=1):
        super().__init__(0)
        self.raio = raio
    
    def perimetro(self):
        return 2 * pi * self.raio
    
    def area(self):
        return pi * self.raio ** 2

