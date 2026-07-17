from retangulo import *
from rich import inspect, print

def main():
    r = Retangulo()

    try:
        r.base = 12
        r.altura = 7
        r.medidas = (8, 12)
    except Exception as e:
        print(f'Ocorreu um erro do tipo {type(e).__name__}: {e}')
    
    print(r.medidas)



if __name__ == '__main__':
    main()
