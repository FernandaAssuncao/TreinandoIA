from sklearn.tree import DecisionTreeClassifier

x = [[c % 2] for c in range(1, 1001)]
y = [1 if c % 2 == 0 else 0 for c in range(1, 1001)]

modelo = DecisionTreeClassifier()
modelo.fit(x, y)

while True:
    numero = int(input('Digite um numero: 999 para sair '))
    if numero == 999:
        break
    else:
        entrada = [[numero % 2]]
        resultado = modelo.predict(entrada)
        if resultado[0] == 1:
            print(f'A IA acha que o numero {numero} foi par')
        else:
            print(f'O IA acha que o numero {numero} foi impar')
