from layers.Layer import Layer as Parent
import numpy as np

class FCLayer(Parent):

    def __init__(self, in_dimensions, out_dimensions):
        self.weights = np.random.rand(in_dimensions, out_dimensions) - 0.5
        self.bias = np.random.rand(1, out_dimensions) - 0.5

    def forward_propagation(self, input):
        '''
        :param x: input_data (X)
        :return: output_data (Y)
        '''
        self.input = input
        self.output = np.dot(self.input, self.weights) + self.bias
        return self.output

    def backward_propagation(self, out_error, rate):
        '''
        :param out_error: ∇L = ∇L(Y)
        :param rate: learning rate in gradient descent
        :return: ∇L = ∇L(X)
        '''
        in_error = np.dot(out_error, self.weights.T)
        weights_error = np.dot(self.input.T, out_error)

        self.weights -= rate * weights_error
        self.bias -= rate * out_error
        return in_error
