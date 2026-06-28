from rich import print
from rich.panel import Panel

class Churraco:
    def __init__(self, pessoas, titulo):
        self.preco_total = 0
        self.pessoas = pessoas
        self.recomendado = 0
        self.titulo = titulo

    def calcular_recomendacao(self):
        self.recomendado = 0.4 * self.pessoas

    def preco(self):
        self.preco_total = self.recomendado * 82.40

    def apresentacao(self):
        self.calcular_recomendacao()
        self.preco()
        caixa = Panel(f'''      Analisando o [red]{self.titulo}[/] para [blue]{self.pessoas}[/] pessoas
        Cada participante comera 0.4 kgs de carne e cada kg custa 82.40
        Recomendo comprar [red]{self.recomendado:.1f}[/]kgs de carne
        O preço total sera de [blue]R${self.preco_total:.2f}[/]
        Cada participante pagara [yellow]{self.preco_total / self.pessoas:.2f}[/] para participar''',
                      title=self.titulo)
        print(caixa)

churraco = Churraco(15, 'Churracos das Divas')
churraco.apresentacao()
