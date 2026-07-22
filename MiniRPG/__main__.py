from personagens import *

if __name__ == '__main__':
    jg1 = Assassino('Heitor Cortês', 9000)
    jg2 = Princesa('Fernanda Assunção', 9000)
    jg2.atacar(jg1, 3000)
    jg1.atacar(jg2, 1200)
    jg1.atacar(jg2, 3000)
    jg2.curar()
    jg1.curar()
