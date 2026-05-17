from rich import print
from rich.traceback import install
install()

def divisao(a, b):
    return a / b

print(divisao(1, 0))
