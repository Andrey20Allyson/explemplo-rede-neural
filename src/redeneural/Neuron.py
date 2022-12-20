from typing import Callable

NeuronFunction = Callable[[list[float], list[float]], float]
ActivationFunction = Callable[[float], float]

def sum_neuron_function(I: list[float], W: list[float]) -> float:
    sum = 0

    for i, w in zip(I, W):
        sum += i * w

    return sum

def step_activation_function(value: float):
    return 0 if value < 0 else value

class Neuron:
    SUM_NF: NeuronFunction = sum_neuron_function

    neuron_function: NeuronFunction
    activation_function: ActivationFunction

    def __init__(self, nFunc: NeuronFunction, aFunc: ActivationFunction):
        self.neuron_function = nFunc

        self.activation_function = aFunc

    def exec(self, I: list[float], W: list[float]):
        return self.activation_function(self.activation_function(I, W))