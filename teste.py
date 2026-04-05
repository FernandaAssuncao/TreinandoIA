from random import randint
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for pos, jogador in enumerate(ranking):
    print(f'{pos + 1} {jogador[0]}: com {jogador[1]} no dado!')
