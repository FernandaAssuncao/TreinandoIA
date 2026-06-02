from sklearn.ensemble import RandomForestClassifier
import customtkinter as ctk

class MatematicaIa:
    def __init__(self):
        self.modelo = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
        self.primo_ou_nao = False
        self.__treinar_ia()

    def __str__(self):
        return 'Uma classe que calcula numeros primos com IA'

    def __gerar_pistas(self, n):
        return [n % 2, n % 3, n % 5, n % 7, n % 11, n % 13, n % 17, n % 19, n % 23, n % 29, n % 31,
                n % 37, n % 41, n % 43, n % 47]

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

        self.ia = MatematicaIa()
        self.title('Matematica')
        self.geometry('450x300')
        self._set_appearance_mode('dark')
        self.columnconfigure(0, weight=1)
        self.titulo = ctk.CTkLabel(self, text='Matematica com IA', text_color='#5DA7E5', fg_color='#1A1A1A',
                              font=('Century Gothic', 25, 'bold'), height=60, corner_radius=10)
        self.titulo.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky='NSEW')

        self.mensagem = ctk.CTkLabel(self, text='Digite um número para saber\n se é primo ou não',
                                text_color='#B4E4FF', font=('Arial', 14, 'bold'))
        self.mensagem.grid(row=2, column=0, columnspan=1, pady=20, padx=20, sticky='NSEW')

        self.campo = ctk.CTkEntry(self, border_color='#00D2FF', border_width=2, corner_radius=15)
        self.campo.grid(row=2, column=2, columnspan=1, pady=20, padx=20, sticky='NSEW')

        self.resposta = ctk.CTkLabel(self, text='', text_color='#B4E4FF', font=('Century Gothic', 14, 'bold'),
                                     )
        self.resposta.grid(row=3, column=0, columnspan=1, pady=20, padx=20, sticky='NSEW')
        self.botao = ctk.CTkButton(self, text='Analisar', command=self.gerar_resposta, fg_color='#3282B8',
                                   hover_color='#0F4C75', corner_radius=15,
                                   font=('Century Gothic', 16, 'bold'))
        self.botao.grid(row=3, column=2, columnspan=1, pady=20, padx=20, sticky='NSEW')

    def gerar_resposta(self):
        try:
            numero = int(self.campo.get())
            self.ia.prever(numero)
            if self.ia.primo_ou_nao:
                cor = '#00FF9F'
                texto = f'O numero {numero} É PRIMO! ✨'
            else:
                cor = '#FF007F'
                texto = f'O numero {numero} É COMPOSTO! ❌'
            self.resposta.configure(text=texto, text_color=cor)
            self.campo.configure(border_color=cor)
        except ValueError:
            self.resposta.configure(text='Erro, digite um valor inteiro!', text_color='#B8405E')
            self.campo.configure(border_color='#B8405E')

if __name__ == '__main__':
    interface = InterfaceMatematica()
    interface.mainloop()
