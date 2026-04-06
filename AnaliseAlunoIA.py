from sklearn.tree import DecisionTreeClassifier

x = [
    [10, 2],
    [3, 10],
    [9, 1],
    [5, 4],
    [6, 5],
    [7, 6],
    [1, 10]
]
y = [1, 0, 1, 0, 1, 1, 0]
modelo = DecisionTreeClassifier()
modelo.fit(x, y)

while True:
    nota = int(input('Digite a nota do aluno: '))
    faltas = int(input('Quantas faltas o aluno teve? (para sair 999)'))
    if faltas == 999:
        break
    else:
        resultado = modelo.predict([[nota, faltas]])
        if resultado == 1:
            print('A IA acha que o aluno vai passar!!')
        else:
            print('A IA acha que o aluno vai reprovar!!')
        correto = str(input('A IA acertou [s/n] ')).strip().lower()
        if correto == 'n':
            certo = int(input('Digite o correto: [1 passou, 0 reprovou] '))
            x.append([nota, faltas])
            y.append(certo)
            modelo.fit(x, y)
            print('A IA aprendeu com voce!!')
            