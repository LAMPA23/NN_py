import numpy as np

def hopfield_train(patterns):
    # Ваги для нейромережі
    num_patterns, pattern_length = patterns.shape
    weights = np.zeros((pattern_length, pattern_length))

    for i in range(num_patterns):
        # Використовуємо зовнішній добуток для оновлення ваг
        weights += np.outer(patterns[i], patterns[i])

    # Забезпечення нулевої діагоналі для ваг
    np.fill_diagonal(weights, 0)

    return weights

def hopfield_recall(weights, patterns, max_iters=10):
    # Ітеративно відновлюємо образи
    num_patterns, pattern_length = patterns.shape
    recalled_patterns = np.zeros_like(patterns)

    for i in range(num_patterns):
        recalled_patterns[i] = patterns[i]

        for _ in range(max_iters):
            # Активація нейронів за допомогою ваг та функції сигнум
            recalled_patterns[i] = np.sign(np.dot(weights, recalled_patterns[i]))

    return recalled_patterns

# Зчитуємо еталонні та спотворені образи з Excel-файлу
reference_A = np.array([[1, -1, 1, -1, 1, -1]])  # Приклад, вам слід замінити це на свої дані
reference_6 = np.array([[-1, 1, 1, 1, 1, -1]])
reference_2 = np.array([[1, 1, 1, -1, -1, 1]])

test_A = np.array([[1, -1, -1, 1, -1, 1]])  # Приклад, вам слід замінити це на свої дані
test_6 = np.array([[-1, 1, -1, -1, 1, 1]])
test_2 = np.array([[1, 1, -1, -1, -1, -1]])

# Об'єднуємо всі образи в один масив
patterns = np.concatenate((reference_A, reference_6, reference_2, test_A, test_6, test_2), axis=0)

# Тренуємо нейромережу
weights = hopfield_train(patterns)

# Відновлюємо образи
recalled_A = hopfield_recall(weights, test_A)
recalled_6 = hopfield_recall(weights, test_6)
recalled_2 = hopfield_recall(weights, test_2)

print("Recalled A:", recalled_A)
print("Recalled 6:", recalled_6)
print("Recalled 2:", recalled_2)
