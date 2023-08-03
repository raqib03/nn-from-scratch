inputs = [1, 2, 3, 2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

layer_outputs = [] # output of the current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    print(f'neuron_weights {neuron_weights}')
    print(f'neuron_bias {neuron_bias}')
    for n_input, weight in zip(inputs, neuron_weights):
        print(f'n_input {n_input}')
        print(f'weight {weight}')
        neuron_output += n_input*weight
        print(f'neuron_output {neuron_output}')
    neuron_output += neuron_bias
    print(f'neuron_output {neuron_output}')
    layer_outputs.append(neuron_output)
    print(f'layer_outputs {layer_outputs}')


print(layer_outputs)