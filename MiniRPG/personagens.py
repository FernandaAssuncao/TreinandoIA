from abc import ABC, abstractmethod
from random import randint, choice
from rich.panel import Panel
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def receber_dano(self, dano):
        fator = randint(1, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print(f'O [blue]{self.nome}[/] levou [red]{fator}[/] dano!')

    def receber_dano_especial(self, dano):
        self.vida = self.vida - dano
        if self.vida < 0:
            self.vida = 0
        print(f'O [blue]{self.nome}[/] levou [red]{dano}[/] dano!')

    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            golpe = choice(self.golpes)
            print(f'O [green]{self.nome}[/] lançou o golpe [yellow]{golpe}[/] em [cyan]{alvo.nome}[/]')
            alvo.receber_dano(forca)
        else:
            print('Não foi possivel realizar esse ataque!')

    def placar(self):
        mensagem = f':white_medium_star: [magenta] Vida: {self.vida}[/]'
        bloco = Panel(mensagem, title=f':sparkles: [purple]{self.__class__.__name__} {self.nome}[/]', width=50)
        print(bloco)

    @abstractmethod
    def curar(self):
        pass

    @abstractmethod
    def ataques_especiais(self, alvo):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida=50):
        super().__init__(nome, vida)
        self.vida_total = vida
        self.golpes = ['soco', 'chute', 'golpe de machado', 'pulo giratorio']

    def curar(self):
        fator = randint(1, 1500)
        self.vida += fator
        if self.vida > self.vida_total:
            self.vida = self.vida_total
        print(f'[cyan]{self.nome}[/] enrolou uma atadura nos ferimentos e [magenta]recuperou {fator} pontos de vida![/]')

    def ataques_especiais(self, alvo):
        fator = randint(4000, 5000)
        print(f'O {self.nome} lançou seu machadao e causou {fator} dano!')
        alvo.receber_dano_especial(fator)


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.vida_total = vida
        self.golpes = ['Bola de fogo', 'Raio de luz', 'magia estatica', 'magia explosiva']

    def curar(self):
        fator = randint(1, 3000)
        self.vida += fator
        if self.vida > self.vida_total:
            self.vida = self.vida_total
        print(f'[cyan]{self.nome}[/] fez uma magia de cura e [magenta]recuperou {fator} pontos de vida![/]')

    def ataques_especiais(self, alvo):
        fator = randint(6000, 7000)
        print(f'O {self.nome} Lançou uma magia de raio explosivo que causou {fator} dano!')
        alvo.receber_dano_especial(fator)


class Assassino(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.vida_total = vida
        self._pontos = 0
        self.golpes = ['Adega Envenenada', 'Ataque Furtivo', 'Golpe de Faca', 'Ataque das Sombras']

    def curar(self):
        fator = randint(1, 2000)
        self.vida += fator
        if self.vida > self.vida_total:
            self.vida = self.vida_total
        print(f'O [magenta]{self.nome}[/] fez curativo para cessar o sagramento e recuperou [green]{fator} pontos de vida[/]')

    @property
    def pontos(self):
        return self._pontos

    @pontos.setter
    def pontos(self, valor=1):
        self._pontos = self._pontos + valor
        if self._pontos > 5:
            self._pontos = 0

    def ganhar_pontos(self):
        self.pontos = 1
        print(f'O [purple]{self.nome}[/] ganhou 1 ponto. Total [blue]{self._pontos}[/] pontos.')

    def ataques_especiais(self, alvo):
        if self._pontos == 5:
            fator = randint(5000, 7000)
            print(f'O {self.nome} lançou sua foice e causou {fator} dano!')
            alvo.receber_dano_especial(fator)
        else:
            print('Pontos insuficientes lançe ataques normais primeiro!')

    def atacar(self, alvo, forca):
        super().atacar(alvo, forca)
        self.ganhar_pontos()
        if self.pontos == 5:
            print(f'[navy_blue]O {self.nome} pode lançar um ataque especial![/]')


class Principe(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.vida_total = vida
        self.golpes = ['Estocada de Florete', 'Corte Elegante', 'Avanço do Nobre', 'Ordem de Batalha']

    def curar(self):
        fator = randint(500, 6000)
        self.vida += fator
        if self.vida > self.vida_total:
            self.vida = self.vida_total
        print(f'O [red]{self.nome}[/] ordenou curandeiros e recuperou [blue]{fator} pontos de vida![/]')

    def ataques_especiais(self, alvo):
        fator = randint(7000, 8000)
        print(f'O {self.nome} pegou sua espada e declarou o avanço da cavalaria real e causou {fator} dano!')
        alvo.receber_dano_especial(fator)


class Princesa(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.vida_total = vida
        self.golpes = ['Luz Majestosa', 'Disparo de Esmeralda', 'Golpe de Cetro', 'Contratar Mercenário']

    def curar(self):
        fator = randint(500, 6000)
        self.vida += fator
        if self.vida > self.vida_total:
            self.vida = self.vida_total
        print(f'O [green]{self.nome}[/] ordenou curandeiros especiais e recuperou [yellow]{fator} pontos de vida![/]')

    def ataques_especiais(self, alvo):
        fator = randint(7000, 8000)
        print(f'A {self.nome} Lançou resgate especial e causou {fator} dano.')
        alvo.receber_dano_especial(fator)
