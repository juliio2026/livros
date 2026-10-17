# ==============================================================================
# Passo 1: Importar Bibliotecas e Carregar Dados
# ==============================================================================
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar o conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# ==============================================================================
# Passo 2: Pré-processamento dos Dados
# ==============================================================================
# Dividir os dados em conjuntos de Treinamento (80%) e Teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados (escala padronizada para melhorar o desempenho da rede neural)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ==============================================================================
# Passo 3: Construir o Modelo (Rede Neural) - Versão Atualizada
# ==============================================================================
model = tf.keras.Sequential([
    # Camada de Entrada explícita (corrige o aviso)
    tf.keras.layers.Input(shape=(4,)),
    # Camada oculta com 8 neurônios e ativação ReLU
    tf.keras.layers.Dense(8, activation='relu'),
    # Camada de saída com 3 neurônios e ativação Softmax
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Compilar o modelo especificando o otimizador, a função de perda e a métrica de avaliação
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ==============================================================================
# Passo 4: Treinar o Modelo
# ==============================================================================
# Treinamento do modelo por 50 épocas
history = model.fit(X_train, y_train, epochs=50, batch_size=16, verbose=1)

# ==============================================================================
# Passo 5: Avaliar o Modelo
# ==============================================================================
# Avaliar a precisão e a perda nos dados de teste que o modelo não viu durante o treino
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n---> Acurácia do modelo nos dados de teste: {accuracy * 100:.2f}%")

# ==============================================================================
# Passo 6: Fazer Previsões
# ==============================================================================
# Testar uma previsão com o primeiro exemplo do conjunto de teste
previsao = model.predict(X_test[:1])
classe_prevista = previsao.argmax(axis=1)[0]
classe_real = y_test[0]

print(f"---> Nome das classes: {iris.target_names}")
print(f"---> Classe Prevista pelo Modelo: {iris.target_names[classe_prevista]}")
print(f"---> Classe Real esperada: {iris.target_names[classe_real]}")
