from rich import print

class Termostato:
    def __init__(self, temperatura=24):
        self.__temperatura = temperatura


    @property
    def ftemperatura(self):
        return f'{self.__temperatura}°C'
    
    @ftemperatura.setter
    def ftemperatura(self):
        return self.__temperatura
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f'Temperatura de {valor}°C é inválida!')
        if valor < 16:
            self.__temperatura = 16
        elif valor > 30:
            self.__temperatura = 30
        else:
            self.__temperatura = valor

