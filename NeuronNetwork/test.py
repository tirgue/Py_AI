from NeuronNetwork import *
from ..ColorRecognition import main

nn = NeuronNetwork(3, 1)

input = np.array([
            [[0],[0],[0]],
            [[0],[0],[1]],
            [[0],[1],[1]],
            [[1],[0],[0]],
            [[1],[1],[0]],
            [[1],[1],[1]],
        ])
output = np.array([
            [0],
            [0],
            [0],
            [1],
            [1],
            [1],
        ])


data1 = np.array([[1],[0],[1]])
data2 = np.array([[0],[1],[0]])

print("Before data 1 : ", np.around(nn.compute(data1), decimals = 2)[0])
print("Before data 2 : ", np.around(nn.compute(data2), decimals = 2)[0])

for k in range(10000):
    for i in range(input.shape[0]):
        nn.train(input[i], output[i])

print("After data 1 : ", np.around(nn.compute(data1), decimals = 2)[0])
print("After data 2 : ", np.around(nn.compute(data2), decimals = 2)[0])
