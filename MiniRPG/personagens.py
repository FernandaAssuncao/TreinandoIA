from abc import ABC, abstractmethod
from random import randint, choice
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

    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            if self.__class__.__name__ == 'Assassino':
                self.ganhar_pontos()
                if self._pontos == 5:
                    self.ataques_especiais()
            golpe = choice(self.golpes)
            print(f'O [green]{self.nome}[/] lançou o golpe [yellow]{golpe}[/] em [cyan]{alvo.nome}[/]')
            alvo.receber_dano(forca)
        else:
            print('Não foi possivel realizar esse ataque!')

    @abstractmethod
    def curar(self):
        pass

    @abstractmethod
    def ataques_especiais(self):
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

    def ataques_especiais(self):
        pass

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

    def ataques_especiais(self):
        pass

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
        if self._pontos > 5:
            self._pontos = 0
        else:
            self._pontos = self._pontos + valor

    def ganhar_pontos(self):
        self.pontos = 1
        print(f'O [purple]{self.nome}[/] ganhou 1 ponto. Total [blue]{self._pontos}[/] pontos.')

    def ataques_especiais(self):
        pass

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

    def ataques_especiais(self):
        pass

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

    def ataques_especiais(self):
        pass
