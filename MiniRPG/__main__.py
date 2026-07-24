from personagens import *

if __name__ == '__main__':
    jg1 = Principe('Heitor Cortês', 9000)
    jg2 = Princesa('Fernanda Assunção', 9000)
    jg1.atacar(jg2, 4000)
    jg2.atacar(jg1, 4000)
    jg2.curar()
    jg1.curar()
    jg1.placar()
    jg2.placar()
