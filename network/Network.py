

class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def add(self, layer):
        self.layers.append(layer)

    def use(self, loss, loss_prime):
        '''
        :param loss: L = L(Y), e.g. MSE
        :param loss_prime:  ∇L = ∇L(Y), e.g ∇MSE(Y)
        :return: void
        '''
        self.loss = loss
        self.loss_prime = loss_prime

    def predict(self, data):
        pass

    def fit(self, x_train, y_train, epochs, alpha):
        '''
        :param x_train: [x_0, x_1, ... , x_{samples - 1}]
        :param y_train: [y_0, y_1, ... , y_{samples - 1}]
        :param epochs: number of iterations (
        :param alpha: weights_(k+1) = weights(k) - alpha * ∇L(weights(k))
        :return:
        '''
        pass