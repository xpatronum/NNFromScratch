import numpy as np

from layers import FCLayer, ActivationLayer

from functions import Activation, ActivationPrime

from functions import Loss, LossPrime

from network import Network

# Training data
x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])

# Network architecture
net = Network()
net.add(FCLayer(2, 3))
net.add(ActivationLayer(Activation.tanh, ActivationPrime.tanh_prime))
net.add(FCLayer(3, 1))
net.add(ActivationLayer(Activation.tanh, ActivationPrime.tanh_prime))

# Train your network
net.use(Loss.mse, LossPrime.mse_prime)
net.fit(x_train, y_train, epochs=1000, alpha=0.1)

# Test
out = net.predict(x_train)
print(out)

