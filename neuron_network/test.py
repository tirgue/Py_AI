try:
    from NeuronNetwork import * 
except:    
    from Py_AI.neuron_network.NeuronNetwork import * 
import random

nn = NeuronNetwork(3, 1, 1, np.array([3]) )

inputs = np.array([
            [0,0,0],
            [0,0,1],
            [0,1,0],
            [0,1,1],
            [1,0,0],
            [1,1,0],
            [1,1,1],
        ])
outputs = np.array([[
            0,
            0,
            0,
            0,
            1,
            1,
            1,
        ]])

# file = open("ColorRecognition/training_datas", "r")
# nb_lines = sum(1 for line in file)

# file.seek(0)

# training_input = np.zeros((nb_lines, 3, 1))
# training_output = np.zeros((nb_lines,1))

# c = 0
# for line in file:
#     r = ''
#     g = ''
#     b = ''
#     rep = ''
#     coma = 0
#     text = ''
#     for i in range(len(line)):
#         if line[i] == ',':
#             if coma == 0:
#                 coma += 1
#                 r = int(text)
#                 text = ''
#             elif coma == 1:
#                 coma += 1
#                 g = int(text)
#                 text = ''
#             else:
#                 coma += 1
#                 b = int(text)
#                 text = ''
        
#         else:
#             text += line[i]
    
#     rep = int(text)
#     if rep == 0:
#         training_output[c] = np.array([[0]])
#     else:
#         training_output[c] = np.array([[1]])

#     training_input[c] = np.array([[r],[g],[b]])
#     c+=1

# print(training_output.shape[0])
# data1 = np.array([[0],[0],[0]]) 
# data2 = np.array([[12],[9],[23]]) 
# data3 = np.array([[23],[26],[45]]) 
# data4 = np.array([[45],[58],[13]]) 
# data5 = np.array([[35],[26],[57]]) 
# data6 = np.array([[12],[8],[1]]) 

# print("Before data 1 : ", np.around(nn.compute(data1), decimals = 15))
# print("Before data 2 : ", np.around(nn.compute(data2), decimals = 15))
# print("Before data 3 : ", np.around(nn.compute(data3), decimals = 15))
# print("Before data 4 : ", np.around(nn.compute(data4), decimals = 15))
# print("Before data 5 : ", np.around(nn.compute(data5), decimals = 15))
# print("Before data 6 : ", np.around(nn.compute(data6), decimals = 15))

data = np.array([[1],[0],[1]])
print("Before data : ", np.round(nn.compute(data), decimals = 15)[0])
c = 0
for k in range(100):
    nn.train(inputs.T, outputs)
    

# print("After data 1 : ", np.around(nn.compute(data1), decimals = 2))
# print("After data 2 : ", np.around(nn.compute(data2), decimals = 2))
# print("After data 3 : ", np.around(nn.compute(data3), decimals = 2))
# print("After data 4 : ", np.around(nn.compute(data4), decimals = 2))
# print("After data 5 : ", np.around(nn.compute(data5), decimals = 2))
# print("After data 6 : ", np.around(nn.compute(data6), decimals = 2))

print("After data : ", np.round(nn.compute(data), decimals = 2))
