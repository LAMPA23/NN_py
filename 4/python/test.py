from neupy import algorithms, layers

# Згенеруйте випадкові дані для прикладу
data = np.random.rand(100, 3)

# Визначте параметри конкурентного шару
num_neurons = 10
learning_rate = 0.01

# Створення та навчання конкурентного шару
network = algorithms.MiniSom(
    n_inputs=3,
    n_outputs=num_neurons,
    learning_rate=learning_rate,
    random_seed=42,
    weight=(0, 1),
    distance='euclid',  # Виберіть відстань, яку ви хочете використовувати
    verbose=True,
)
network.train(data, epochs=100)

# Отримання ваг конкурентного шару після навчання
competitive_layer_weights = network.weights
print(competitive_layer_weights)