import os
from sklearn.ensemble import RandomForestClassifier
from random import randint, choice
import joblib


class IAFinanceira:
    nome_arquivo = 'modelo_sistema_financeiro.joblib'
    arquivo_dados = 'historico_credito.csv'

    def __init__(self):
        self.__modelo = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
        self.__treinada = False
        self.verificar()

    def __treinar_ia(self):
        x = []
        y = []
        for c in range(1, 7000):
            idade = randint(18, 80)
            salario = randint(1200, 50000)
            valor_solicitado = randint(5000, 200000)
            nome_limpo = choice([0, 1])
            if nome_limpo == 0 or valor_solicitado > (salario * 10):
                resultado = 0
            else:
                resultado = 1
            x.append([idade, salario, valor_solicitado, nome_limpo])
            y.append(resultado)
        self.__modelo.fit(x, y)
        self.__treinada = True

    def prever(self, idade:int, salario:float, valor:float, nome_limpo:int):
        resultado = self.__modelo.predict([[idade, salario, valor, nome_limpo]])
        return resultado[0] == 1 #Retorna 1 se for aprovado.

    def __salvar_modelo(self):
        joblib.dump(self.__modelo, self.nome_arquivo)

    def verificar(self):
        if os.path.exists(self.nome_arquivo):
            self.__modelo = joblib.load(self.nome_arquivo)
            self.__treinada = True
            print('Modelo carregado com sucesso!')
        else:
            self.__treinar_ia()
            self.__salvar_modelo()
            print('Modelo treinado e salvo com sucesso!')

    def calcular_probabilidade(self, idade:int, salario:float, valor:float, nome_limpo:int):
        resultado = self.__modelo.predict_proba([[idade, salario, valor, nome_limpo]])
        return resultado[0][1]

    def __atualizar_historico(self):
        self.__treinar_ia()
        self.__salvar_modelo()
