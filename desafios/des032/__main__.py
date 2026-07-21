from ContaBancaria import *

def main():
    cc = ContaBancaria(000, 'Marcelo', 10000, 'Guanabara')
    cc.sacar(500)
    
    print('Tentando mudar o nome')
    cc.nome = 'Maricota'
    
    print(cc)

if __name__ == '__main__':
    main()
