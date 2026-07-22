from sklearn.tree import DecisionTreeClassifier

x = [[c] for c in range(1, 1001)]
y = [1 if c % 2 == 0 else 0 for c in range(1, 1001)]

modelo = DecisionTreeClassifier()
modelo.fit(x, y)

while True:
    numero = int(input('Digite um numero: 999 para sair '))
    if numero == 999:
        break
    else:
        entrada = [[numero]]
        resultado = modelo.predict(entrada)
        if resultado[0] == 1:
            print(f'A IA acha que o numero {numero} foi par')
        else:
            print(f'O IA acha que o numero {numero} foi impar')
        correto = str(input('A IA acertou? [s/n] ')).strip().lower()
        if correto == 'n':
            certo = int(input('Digite o correto: [1 par] [0 impar] '))
            x.append([numero])
            y.append(certo)
            modelo.fit(x, y)
            print('A IA aprendeu com voce!!')
