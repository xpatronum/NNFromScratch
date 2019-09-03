
class LossPrime:

    @staticmethod
    def mse_prime(y_true, y_pred):
        '''
        :param y_true: True label for fixed input.
        :param y_pred: Predicted output of the network (e.g y_pred = net.predict(x))
        :return: ∇L(Y)
        '''
        return 2 * (y_pred - y_true) / (y_true.size)