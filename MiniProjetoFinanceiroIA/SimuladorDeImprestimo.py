from ClienteSistema import PropostaImprestimo
from IASimuladorDeImprestimo import IAFinanceira
import customtkinter as ctk
from GerenciadorDeDados import GerenciarDados


class InterfaceSimuladorImprestimo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.ia = IAFinanceira()

        self.title('Simulador de Imprestimo')
        self.geometry('550x550')
        self._set_appearance_mode('dark')
        self.columnconfigure(0, weight=1)

        self.titulo = ctk.CTkLabel(self, text='Simulador de Imprestimo IA', text_color='#00BFFF', fg_color='#1A1A1A',
                                   font=('Century Gothic', 25, 'bold'), height=60, corner_radius=15)
        self.titulo.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky='nsew')

        self.mensagem = ctk.CTkLabel(self, text='Digite abaixo as informações solicitadas: IDADE',
                                     text_color='#1E90FF', font=('Arial', 15, 'bold'))
        self.mensagem.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

        self.campo_idade = ctk.CTkEntry(self, border_color='#00BFFF', border_width=2,
                                        corner_radius=50)
        self.campo_idade.grid(row=1, column=2, columnspan=1, padx=20, pady=20, sticky='nsew')
        self.campo_idade.bind("<Return>", lambda event: self.campo_salario.focus_set())

        self.mensagem2 = ctk.CTkLabel(self, text='SALARIO: ', text_color='#1E90FF',
                                      font=('Arial', 15, 'bold'))
        self.mensagem2.grid(row=2, column=0, columnspan=1, padx=20, pady=20, sticky='nsew')

        self.campo_salario = ctk.CTkEntry(self, border_color='#00BFFF', border_width=2,
                                          corner_radius=50)
        self.campo_salario.grid(row=2, column=2, padx=20, pady=20, sticky='nsew')
        self.campo_salario.bind("<Return>", lambda event: self.campo_valor.focus_set())

        self.mensagem3 = ctk.CTkLabel(self, text='VALOR DO IMPRESTIMO: ', text_color='#1E90FF',
                                      font=('Arial', 15, 'bold'))
        self.mensagem3.grid(row=3, column=0, columnspan=1, padx=20, pady=20, sticky='nsew')

        self.campo_valor = ctk.CTkEntry(self, border_color='#00BFFF', border_width=2,
                                        corner_radius=50)
        self.campo_valor.grid(row=3, column=2, columnspan=1, padx=20, pady=20, sticky='nsew')
        self.campo_valor.bind("<Return>", lambda event: self.gerar_resposta())


        self.mensagem4 = ctk.CTkLabel(self, text='SEU NOME ESTÁ LIMPO?\n [SIM] ligado e [NÃO] desligado ',
                                      text_color='#1E90FF', font=('Arial', 15, 'bold'))
        self.mensagem4.grid(row=4, column=0, columnspan=1, padx=20, pady=20, sticky='nsew')

        self.switch_nome_limpo = ctk.CTkSwitch(
            self,
            text="Nome Limpo",
            font=('Arial', 14, 'bold'),
            progress_color='#00BFFF'  # Cor quando estiver ligado
        )
        self.switch_nome_limpo.grid(row=4, column=2, columnspan=2, padx=20, pady=20, sticky='nsew')

        self.resposta = ctk.CTkLabel(self, text='', text_color='#1E90FF', font=('Arial', 15, 'bold'))
        self.resposta.grid(row=5, column=0, columnspan=2, padx=20, pady=20, sticky='nsew')

        self.botao = ctk.CTkButton(self, command=self.gerar_resposta, text='ANALISAR',
                                   text_color='white', fg_color='#00BFFF',
                                   border_color='#00FFFF', corner_radius=15, border_width=2,
                                   font=('Century Gothic', 19, 'bold'), hover_color='#008B8B')
        self.botao.grid(row=5, column=2, columnspan=2, padx=20, pady=20, sticky='nsew')


    def gerar_resposta(self):
        try:
            idade = int(self.campo_idade.get())
            salario = float(self.campo_salario.get())
            valor = float(self.campo_valor.get())
            nome_limpo = int(self.switch_nome_limpo.get())
            cliente = PropostaImprestimo(idade, salario, nome_limpo, valor)
            previsao = self.ia.prever(idade, salario, valor, nome_limpo)
            if previsao:
                cliente.status = 'aprovado'
                cor = '#7FFFD4'
                texto = f'Parabens, o imprestimo no valor de R${cliente.valor_solicitado}\n foi {cliente.status}.'
            else:
                cliente.status = 'reprovado'
                cor = '#9B111E'
                texto = f'Sinto muito, o imprestimo no valor de R${cliente.valor_solicitado}\n foi {cliente.status}.'
            self.resposta.configure(text=texto, text_color=cor)
            self.campo_idade.configure(border_color=cor)
            self.campo_salario.configure(border_color=cor)
            self.campo_valor.configure(border_color=cor)
            g = GerenciarDados()
            g.salvar_novo_dado(cliente.idade, cliente.salario, cliente.valor_solicitado,
                               cliente.nome_limpo, cliente.status)
        except ValueError:
            cor = '#FF3B30'
            self.campo_idade.configure(border_color=cor)
            self.campo_salario.configure(border_color=cor)
            self.campo_valor.configure(border_color=cor)
            self.resposta.configure(text='ERRO, por favor digite\n oque se pede corretamente!',
                                    text_color=cor)

if __name__ == '__main__':
    tela = InterfaceSimuladorImprestimo()
    tela.mainloop()
