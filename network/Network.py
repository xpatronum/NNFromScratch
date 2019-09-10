

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
        samples = len(data)
        result = []

        # For every training vector data x_i do:
        for i in range(samples):
            # Forward propagation
            output = data[i]
            for layer in self.layers:
                output = layer.forward_propagation(output)
            result.append(output)
        return result

    def fit(self, x_train, y_train, epochs, alpha):
        '''
        :param x_train: [x_0, x_1, ... , x_{samples - 1}]
        :param y_train: [y_0, y_1, ... , y_{samples - 1}]
        :param epochs: number of iterations (
        :param alpha: weights_(k+1) = weights(k) - alpha * ∇L(weights(k))
        :return:
        '''
        samples = len(x_train)

        # For every training cycle -> forward() -> forward() -> Loss() <- backward() <- backward() ...
        for i in range(epochs):
            error = 0
            for k in range(samples):
                # Forward propagation
                output = x_train[k]
                for l in self.layers:
                    # Output of the previous layer => input to the current layer @l
                    output = l.forward_propagation(output)
                # Total error after current x_k has passed training cycle.
                error += self.loss(y_train[k], output)

                # Backward propagation
                gradient = self.loss_prime(y_train[k], output)
                for l in reversed(self.layers):
                    gradient = l.backward_propagation(gradient, alpha)

            # What is the total average error after one epoch ?
            error /= samples
            print('On epoch ' + str(i + 1) + ' an average error = ' + str(error))