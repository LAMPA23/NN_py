import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def plot_interpolated_vectors(vector1, vector2):
    # Генерація значень x для інтерполяції
    x = np.linspace(0, len(vector1) - 1, len(vector1))

    # Створення функцій інтерполяції для обох векторів
    interp_func1 = interp1d(x, vector1, kind='linear', fill_value='extrapolate')
    interp_func2 = interp1d(x, vector2, kind='linear', fill_value='extrapolate')

    # Генерація значень x для виведення на графіку
    x_values = np.linspace(0, len(vector1) - 1, 1000)

    # Отримання інтерпольованих значень для обох векторів
    y_interp1 = interp_func1(x_values)
    y_interp2 = interp_func2(x_values)

    # Вивід графіків
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_interp1, label='Математично обраховані центроїди')
    plt.plot(x_values, y_interp2, label='Центроїди отримані задопомогою НМ КК')
    plt.scatter(x, vector1, color='red', marker='o')
    plt.scatter(x, vector2, color='blue', marker='o')

    plt.title('Порівняння центроїдів')
    plt.xlabel('Координата')
    plt.ylabel('Значення')
    plt.legend()
    plt.grid(True)
    plt.show()

