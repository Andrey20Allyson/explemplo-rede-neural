# from redeneural.NeuralNetwork import NeuralNetwork
import random

weights = [2., -4.]

def neuron(I: list[float], W: list[float]):
    sum = float(0)

    for i, w in zip(I, W):
        sum += i * w

    return float(0) if sum < 0 else sum

results = []

for i in range(10):
    result = neuron([random.randint(0, 10), random.randint(0, 20)], weights)

    results.append(result)

print(results)