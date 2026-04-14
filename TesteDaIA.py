from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# dados
X = [
    [8, 2, 3],
    [7, 3, 2],
    [9, 1, 4],
    [5, 6, 1],
    [4, 8, 0],
    [3, 10, 0],
    [6, 4, 2],
    [2, 9, 0],
    [10, 20, 3],
    [10, 2, 5]
]

y = [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]

# dividir
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)

# treinar
modelo = DecisionTreeClassifier()
modelo.fit(X_treino, y_treino)

# testar
previsoes = modelo.predict(X_teste)

# avaliar
print("Precisão:", accuracy_score(y_teste, previsoes))
