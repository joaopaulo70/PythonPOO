from rich import inspect
from poligono import *

def main():
    q = Quadrado(20)

    print(f'Um quadrado de lado {q.lado}cm tem um perímetro de {q.perimetro():.1f}cm')
    print(f'Um quadrado de lado {q.lado}cm tem uma área de {q.area():.1f}cm²')
    # inspect(q, methods=True)

    c = Circulo(12)
    print(f'Um círculo de raio {c.raio}cm tem um perímetro de {c.perimetro():.1f}cm')
    print(f'Um círculo de raio {c.raio}cm tem uma área de {c.area():.1f}cm²')
    # inspect(c, methods=True)

if __name__ == "__main__":
    main()
