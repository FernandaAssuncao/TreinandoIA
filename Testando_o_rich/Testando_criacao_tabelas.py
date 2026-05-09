from rich import print
from rich.table import Table

tabela = Table(title=' Tabelas de Preços')
tabela.add_column('nome', justify='center')
tabela.add_column('valor', justify='center')

tabela.add_row('Lapis', 'R$7.50')
tabela.add_row('Borracha', 'R$9.50')
print(tabela)
