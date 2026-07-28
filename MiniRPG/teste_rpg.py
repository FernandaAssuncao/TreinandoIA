from personagens import *

if __name__ == '__main__':
    jg1 = Principe('Heitor Cortês', 9000)
    jg2 = Princesa('Fernanda Assunção', 9000)

    mens1= jg1.atacar(jg2, 4000)
    print(mens1)
    mens2 = jg2.atacar(jg1, 4000)
    mens3 = jg2.curar()
    mens4 = jg1.curar()
    jg1.placar()
    jg2.placar()
