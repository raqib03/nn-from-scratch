import math

softmax_output = [0.7, 0.1, 0.2]
target_output = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

print(f'loss = {loss}')

loss1 = -math.log(softmax_output[0])
print(f'loss1 = {loss1}')

loss2 = -math.log(softmax_output[1])
print(f'loss2 = {loss2}')

loss3 = -math.log(softmax_output[2])
print(f'loss3 = {loss3}')