import os
from sklearn.ensemble import RandomForestClassifier
from random import randint, choice
import customtkinter as ctk
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
        return resultado[0][0]

    def __atualizar_historico(self):
        self.__treinar_ia()
        self.__salvar_modelo()


class InterfaceSimuladorImprestimo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.ia = IAFinanceira()

        self.title('Simulador de Imprestimo')
        self.geometry('550x450')
        self._set_appearance_mode('dark')
        self.columnconfigure(0, weight=1)

        self.titulo = ctk.CTkLabel(self, text='Simulador de Imprestimo', text_color='#00BFFF', fg_color='#1A1A1A',
                                   font=('Century Gothic', 25, 'bold'), height=60, corner_radius=15)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky='nsew')

        self.mensagem = ctk.CTkLabel(self, text='Digite abaixo as informações solicitadas: IDADE',
                                     text_color='#1E90FF', font=('Arial', 15, 'bold'))
        self.mensagem.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

        self.campo_idade = ctk.CTkEntry(self, border_color='#00BFFF', border_width=2,
                                        corner_radius=50)
        self.campo_idade.grid(row=1, column=2, columnspan=1, padx=20, pady=20, sticky='nsew')

        self.mensagem2 = ctk.CTkLabel(self, text='SALARIO: ', text_color='#1E90FF',
                                      font=('Arial', 15, 'bold'))
        self.mensagem2.grid(row=2, column=0, columnspan=1, padx=20, pady=20, sticky='nsew')

        self.campo_salario = ctk.CTkEntry(self, border_color='#00BFFF', border_width=2,
                                          corner_radius=50)
        self.campo_salario.grid(row=2, column=2, padx=20, pady=20, sticky='nsew')


if __name__ == '__main__':
    tela = InterfaceSimuladorImprestimo()
    tela.mainloop()
