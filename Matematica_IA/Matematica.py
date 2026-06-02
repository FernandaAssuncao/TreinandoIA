from sklearn.ensemble import RandomForestClassifier
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

def pausa_ia(funcao):
    def wrapper(*args, **kwargs):
        print('🤖 A IA esta processando', end='')
        for _ in range(4):
            print('.', end='', flush=True)
            sleep(0.4)
        print('\n')
        return funcao(*args, **kwargs)
    return wrapper

class Matematica:
    def __init__(self):
        self.numero = 0
        self.divisores = []
        self.primo_ou_nao = ''
        self.raiz_quadrada = 0
        self.modelo = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
        self.treinado = False

    def __str__(self):
        return f'O objeto matematico configuardo para o numero {self.numero}'

    def mudar_numero(self, numero):
        if len(self.divisores) != 0:
            self.divisores.clear()
        self.numero = numero

    def __gerar_pistas(self, n):
        return [n % 2, n % 3, n % 5, n % 7, n % 11, n % 13, n % 17, n % 19, n % 23, n % 29, n % 31]

    def __treinar_ia(self):
        y = []
        x = []
        for c in range(1, 2001):
            pista = self.__gerar_pistas(c)
            x.append(pista)
            d = [i for i in range(1, int(sqrt(c)) + 1) if c % i == 0]
            y.append(1 if len(d) == 1 and c > 1 else 0)
        self.modelo.fit(x, y)
        self.treinado = True

    @pausa_ia
    def sugerir_proximo_numero_ia(self):
        if not self.treinado:
            self.__treinar_ia()
        distancia = 1
        while True:
            vizinhos = [self.numero + distancia, self.numero - distancia]
            for v in vizinhos:
                if v > 2:
                    pistas = [self.__gerar_pistas(v)]
                    if self.modelo.predict(pistas)[0] == 1:
                        print(f'DICA DA IA 🤖: O numero {self.numero} não é primo!')
                        print(f'Mas eu encontrei o numero {v} que parece ser!')
                        while True:
                            decisao = str(input('Deseja mudar para ele? [s/n] ')).strip().lower()
                            if decisao == 'n' or decisao == 's':
                                break
                            else:
                                print('Erro digite uma opção valida')
                        if decisao == 's':
                            self.mudar_numero(numero=v)
                            print(f'Numero alterado para {self.numero} com sucesso!')
                        return
            distancia += 1
            if distancia == 20:
                print(f'🤖 A IA nao encontrou nenhum numero primo por perto!')
                break

    @pausa_ia
    def palpite_ia(self):
        if not self.treinado:
            self.__treinar_ia()
        pistas_atuais = [self.__gerar_pistas(self.numero)]
        previsao = self.modelo.predict(pistas_atuais)
        if previsao[0] == 1:
            print(f'🤖 A IA acha que o numero {self.numero} É PRIMO!')
        else:
            print(f'🤖 A IA acha que o numero {self.numero} NÃO É PRIMO!')

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

if __name__ == '__main__':
    mat = Matematica()
    while True:
        print('=' * 25)
        print(''' MATEMATICANDO 
        [1] mudar numero
        [2] divisores
        [3] primo ou nao? 
        [4] raiz quadrada
        [5] 🤖 palpite IA
        [6] 🤖 Encontrar numeros primos proximos
        [7] sair''')
        print('=' * 25)
        try:
            opcao = int(input('Digite uma opcao: '))
        except ValueError:
            print('Opcao invalida!')
            continue
        else:
            if opcao == 1:
                num = int(input('Digite um numero: '))
                mat.mudar_numero(num)
            elif opcao == 2:
                mat.mostrar_divisores()
            elif opcao == 3:
                mat.verificar_primo_ou_nao()
            elif opcao == 4:
                mat.raiz_quadradaa()
            elif opcao == 5:
                mat.palpite_ia()
            elif opcao == 6:
                mat.sugerir_proximo_numero_ia()
            elif opcao == 7:
                break
            else:
                print('Opcao invalida!')
