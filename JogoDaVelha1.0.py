from random import choice


class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [''] * 9
        self.jogador = 'X'
        self.computador = 'O'

    def mostrar_tabuleiro(self):
        for c in range(0, 9):
            print(f'{self.tabuleiro[c]} | ', end='')
            if c == 2 or c == 5 or c == 8:
                print('\n')

    def verificar_posicao_jogador(self):
        try:
            escolha = int(input('Digite um número de 0 a 8: '))
            if self.tabuleiro[escolha] == '':
                self.tabuleiro[escolha] = self.jogador
            else:
                raise
        except:
            print('\033[1:31mErro, por favor digite oque se pede!!\033[m')

    def verificar_posicao_computador(self):
        livres = [i for i in range(0, 9) if self.tabuleiro[i] == '']
        pos = choice(livres)
        print(f'O computador escolheu: {pos}')
        self.tabuleiro[pos] = self.computador

    def jogar(self):
        for c in range(0, 9):
            self.mostrar_tabuleiro()
            self.verificar_posicao_jogador()
            self.verificar_posicao_computador()
            if '' not in self.tabuleiro:
                break



jogo = JogoDaVelha()
jogo.jogar()
