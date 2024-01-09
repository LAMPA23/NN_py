from minisom import MiniSom
import numpy as np

def get_som(mixed_noise_matrix):
    som = MiniSom(3, 1, input_len=mixed_noise_matrix.shape[1], sigma=1.0, learning_rate=0.5)
    som.train_random(mixed_noise_matrix, 1000) 
    som_map = som.get_weights()
    return som_map[0,0], som_map[1,0], som_map[2,0],