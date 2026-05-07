from time import sleep
from math import sqrt

def pausa(funcao):
    def wrapper(*args, **kwargs):
        print('Calculando...', end='')
        for _ in range(3):
            print('.', end='', flush=True)
            sleep(0.5)
        print(end='\n')
        return funcao(*args, **kwargs)
    return wrapper

class Matematica:
    def __init__(self):
        self.numero = 0
        self.divisores = []
        self.primo_ou_nao = ''
        self.raiz_quadrada = 0

    def __str__(self):
        return f'O objeto matematico configuardo para o numero {self.numero}'

    def mudar_numero(self, numero):
        if len(self.divisores) != 0:
            self.divisores.clear()
        self.numero = numero

    @pausa
    def raiz_quadradaa(self):
        self.raiz_quadrada = sqrt(self.numero)
        print(f'A raiz quadrada de {self.numero} é {self.raiz_quadrada}')

    def __calcular_divisores(self):
        for c in range(self.numero, 0, -1):
            if self.numero % c == 0:
                self.divisores.append(c)

    @pausa
    def verificar_primo_ou_nao(self):
        if len(self.divisores) == 0:
            self.__calcular_divisores()
        if len(self.divisores) == 2:
            print(f'O numero {self.numero} É PRIMO!')
        else:
            print(f'O numero {self.numero} NÃO É PRIMO!')

    @pausa
    def mostrar_divisores(self):
        if self.numero != 0:
            if len(self.divisores) > 0:
                pass
            else:
                self.__calcular_divisores()
            print(f'Os divisores de {self.numero} são ', end='')
            for c in self.divisores:
                print(f'{c}', end=',')
            print(end='\n')
        else:
            print('Erro, mude o numero!')


mat = Matematica()
while True:
    print('=' * 25)
    print(''' MATEMATICANDO 
    [1] mudar numero
    [2] divisores
    [3] primo ou nao? 
    [4] raiz quadrada
    [5] sair''')
    print('=' * 25)
    try:
        opcao = int(input('Digite uma opcao:'))
    except ValueError:
        print('Opcao invalida!')
        continue
    else:
        if opcao == 1:
            num = int(input('Digite um numero:'))
            mat.mudar_numero(num)
        elif opcao == 2:
            mat.mostrar_divisores()
        elif opcao == 3:
            mat.verificar_primo_ou_nao()
        elif opcao == 4:
            mat.raiz_quadradaa()
        elif opcao == 5:
            break
        else:
            print('Opcao invalida!')
