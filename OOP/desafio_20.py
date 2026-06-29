from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []
        self.mensagem = ''

    def adicionar_jogo(self, nome):
        self.jogos_favoritos.append(nome)
        self.jogos_favoritos.sort()

    def __mensagem(self):
        self.mensagem = f'nome real: [blue]{self.nome}[/]\nJogos favoritos: \n'
        for c in self.jogos_favoritos:
            self.mensagem += f':laptop_computer:[red]{c}[/]\n'

    def ficha(self):
        self.__mensagem()
        caixa = Panel(f'{self.mensagem}', title=f'Jogador {self.nick}', width=34)
        print(caixa)


jogador1 = Gamer('Fernanda', 'diva')
jogador1.adicionar_jogo('The sims 4')
jogador1.adicionar_jogo('Free Fire')
jogador1.adicionar_jogo('Stardew Valley')
jogador1.ficha()

jogador2 = Gamer('Heitor', 'divo')
jogador2.adicionar_jogo('Stardew Valley')
jogador2.adicionar_jogo('Brawl stars')
jogador2.ficha()
