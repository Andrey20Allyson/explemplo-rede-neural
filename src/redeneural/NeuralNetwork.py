from redeneural.Neuron import Neuron

class NeuralNetwork:
    weights: list[list[list[float]]]
    neurons: Neuron

    nInputs: int
    nOutputs: int

    def __init__(self, nInputs, nOutputs) -> None:
        self.nInputs = nInputs
        self.nOutputs = nOutputs
