import numpy as np

class ActivationPrime:

    @staticmethod
    def tanh_prime(x):
        return 1 - np.tanh(x) ** 2