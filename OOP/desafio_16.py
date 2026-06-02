from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        print(f':waving_hand_light_skin_tone: Olá eu sou [red]{self.nome}[/red] e sou {self.cargo} do setor de  {self.setor}')

f1 = Funcionario('Fernanda', 'TI', 'Scrum Master')
f1.apresentacao()

f2 = Funcionario('Heitor', 'Liderança', 'CEO')
f2.apresentacao()
