from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        painel = Panel(f'{self.nome.center(30)}\n valor: {self.valor}' , title='Produto', width=34)
        print(painel)

p1 = Produto('Iphone 16 pro max', 7500.00)
p1.etiqueta()

p2 = Produto('Mouse', 120.99)
p2.etiqueta()
