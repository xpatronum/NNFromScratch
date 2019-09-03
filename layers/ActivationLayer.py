from layers.Layer import Layer as Parent

class ActivationLayer(Parent):

    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward_propagation(self, input):
        '''
        :param input:
        :return:
        '''
        self.input = input
        self.output = self.activation(self.input)
        return self.output

    def backward_propagation(self, out_error, rate):
        '''

        :param out_error:
        :param rate: learning_rate
        :return:
        '''
        return self.activation_prime(self.input) * out_error
