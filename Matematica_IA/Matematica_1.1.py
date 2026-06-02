from sklearn.ensemble import RandomForestClassifier
import customtkinter as ctk
import os


class Matematica:
    @staticmethod
    def __gerar_pistas(n):
        return [n % 2, n % 3, n % 5, n % 7, n % 11, n % 13, n % 17, n % 19, n % 23, n % 29, n % 31,
                n % 37, n % 41, n % 43, n % 47]

    def __init__(self):
        self.modelo = RandomForestClassifier(n_estimators=100, max_depth=14, random_state=42)
        self.primo_ou_nao = False
        self.__treinar_ia()

    def __treinar_ia(self):
        x = []
        y = []
        for c in range(1, 3001):
            pistas = self.__gerar_pistas(c)
            x.append(pistas)
            d = [i for i in range(c, 0, -1) if c % i == 0]
            y.append(1 if len(d) == 2 else 0)
        self.modelo.fit(x, y)

    def prever(self, numero):
        pistas = [self.__gerar_pistas(numero)]
        resultado = self.modelo.predict(pistas)
        if resultado[0] == 1:
            self.primo_ou_nao = True
        else:
            self.primo_ou_nao = False


class InterfaceMatematica(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.ia = Matematica()
        self.arquivo_historico = 'Historico.text'

        self.title('Matematica')
        self.geometry('450x450')
        self._set_appearance_mode('dark')
        self.columnconfigure(0, weight=1)

        self.frame = ctk.CTkFrame(self, border_color='#C71585', border_width=1)
        self.frame.grid(row=1, column=0, columnspan=4, pady=20, padx=20, sticky='nsew')

        self.titulo_frame = ctk.CTkLabel(self.frame, text='Historico de Numeros', text_color='#C71585',
                                         font=('Century Gothic', 15, 'bold'), height=40, corner_radius=10)
        self.titulo_frame.grid(row=0, column=0, columnspan=2, pady=20, padx=20)

        self.conteudo_frame = ctk.CTkLabel(self.frame, text='', text_color='#DB7093',
                                           font=('Arial', 12, 'bold'))
        self.conteudo_frame.grid(row=0, column=2, columnspan=2, pady=20, padx=20)

        self.atualizar_historico()

        self.titulo = ctk.CTkLabel(self, text='Matematica com IA', text_color='#FF1493', fg_color='#1A1A1A',
                                   font=('Century Gothic', 25, 'bold'), height=60, corner_radius=20)
        self.titulo.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky='nsew')

        self.mensagem = ctk.CTkLabel(self, text='Digite um número para saber\n se é primo ou composto!',
                                     text_color='#DB7093', font=('Arial', 12, 'bold'))
        self.mensagem.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky='nsew')

        self.campo = ctk.CTkEntry(self, border_color='#FF1493', border_width=2, corner_radius=50)
        self.campo.grid(row=2, column=2, columnspan=2, pady=20, padx=20, sticky='nsew')

        self.resposta = ctk.CTkLabel(self, text='', text_color='#FF1493', font=('Arial', 12, 'bold'))
        self.resposta.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky='nsew')

        self.botao = ctk.CTkButton(self, text='Analisar', command=self.gerar_resposta, fg_color='#FF1493',
                                   corner_radius=15, font=('Century Gothic', 14, 'bold'),
                                   border_color='#FF69B4', border_width=1, hover_color='#C71585')
        self.botao.grid(row=3, column=2, columnspan=1, pady=20, padx=20, sticky='nsew')

    def gerar_resposta(self):
        try:
            numero = int(self.campo.get())
            self.ia.prever(numero)
            if self.ia.primo_ou_nao:
                texto = f'A IA acha que o numero {numero}\n É PRIMO!!'
                text_res = 'PRIMO'
                cor = '#00FF00'
            else:
                texto = f'A IA acha que o número {numero}\n É COMPOSTO!'
                text_res = 'COMPOSTO'
                cor = '#FF4444'
            self.resposta.configure(text=texto, text_color=cor)
            self.campo.configure(border_color=cor)
            self.adicionar_no_arquivo(numero, text_res)
            self.atualizar_historico()
        except ValueError:
            self.resposta.configure(text='ERRO, DIGITE UM VALOR INTEIRO', text_color='#FF0000')
            self.campo.configure(border_color='#FF0000')

    def atualizar_historico(self):
        if not os.path.exists(self.arquivo_historico):
            with open(self.arquivo_historico, 'w') as f:
                pass

        with open(self.arquivo_historico, 'r', encoding='UTF-8') as arquivo:
            conteudo = arquivo.read()

        self.conteudo_frame.configure(text=conteudo)

    def adicionar_no_arquivo(self, numero, resposta_texto):
        with open(self.arquivo_historico, 'a', encoding='UTF-8') as arquivo:
            arquivo.write(f'{numero}: {resposta_texto}\n')

if __name__ == '__main__':
    interface = InterfaceMatematica()
    interface.mainloop()
