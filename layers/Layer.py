
# Abstract base class
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    # Computes the output Y of a layer for a given input X
    def forward_propagation(self, input):
        '''
        :param input: X
        :return: Y
        '''
        pass

    def backward_propagation(self, out_error, rate):
        '''
        :param out_error: ∇L = ∇L(Y).
        :param rate: learning rate in gradient descent
        :return: ∇L = ∇L(X)
        '''
        pass

