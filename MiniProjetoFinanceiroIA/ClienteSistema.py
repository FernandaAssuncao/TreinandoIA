from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, idade:int, salario:float, nome_limpo:int):
        self._idade = idade
        self._salario = salario
        self._nome_limpo = nome_limpo


class PropostaImprestimo(Cliente):
    def __init__(self, idade:int, salario:float, nome_limpo:int, valor:float):
        super().__init__(idade, salario, nome_limpo)
        self.valor_solicitado = valor
        self.status = 'pendente'
        