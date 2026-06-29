from time import sleep
from rich import print


class Livro:
    def __init__(self, nome, paginas):
        self.nome_livro = nome
        self.paginas_total = paginas
        self.pagina = 1
        self.mostrar_tela = 1

    def __apresentacao(self):
        print(f'Voce acabou de abrir o livro {self.nome_livro} que tem {self.paginas_total} paginas.E agora voce esta na pagina {self.pagina}')

    def avancar_pagina(self, quantidade):
        self.__apresentacao()
        if (self.pagina + quantidade) >= self.paginas_total:
            print(f'[red]Você já terminou o livro {self.nome_livro}, não pode mais avançar[/]')
            self.pagina = self.paginas_total
        else:
            self.pagina += quantidade
            for c in range(1, quantidade):
                self.mostrar_tela += 1
                sleep(0.5)
                print(f'pagina [blue]{self.mostrar_tela}[/] > ', end='')
        print(f'Agora voce está na pagina [black]{self.pagina}[/]')

livro = Livro('A bela adormecida', 50)
livro.avancar_pagina(5)
livro.avancar_pagina(10)
