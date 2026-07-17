class Retangulo:
    def __init__(self, base=1, altura=1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        if not isinstance(base, float) and not isinstance(base, int):
            raise TypeError('O valor da base deve ser um número')
        if base < 0:
            raise ValueError('Valor inválido para a base')
        else:
            self._base = base

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        if not isinstance(altura, float) and not isinstance(altura, int):
            raise TypeError('O valor da altura deve ser um número')
        if altura < 0:
            raise ValueError('Valor inválido para a altura')
        else:
            self._altura = altura

    @property
    def medidas(self):
        return f'Base = {self.base} \nAltura = {self.altura} \nÁrea = {self.area}'

    @medidas.setter
    def medidas(self, dados:tuple):
        if not isinstance(dados, tuple):
            raise TypeError('As medidas devem ser informadas dentro de uma tupla')
        if len(dados) != 2:
            raise SyntaxError('Informe uma tupla com apenas dois valores numéricos')
        if isinstance(dados[0], float) or isinstance(dados[0], int):
            self.base = dados[0]
        else:
            raise TypeError('A base deve ser um número')
        if isinstance(dados[1], float) or isinstance(dados[1], int):
            self.altura = dados[1]
        else:
            TypeError('A altura deve ser um número')

    @property
    def area(self):
        return self.base * self.altura
    
    @area.setter
    def area(self):
        raise PermissionError('Área não pode ser configurada desse jeito')
    