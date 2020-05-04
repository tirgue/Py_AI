from .Individual import *
import numpy as np
import copy
import random

class Genetic(object):
    
    def __init__(self, nb_population, neuron_network_params):
        self.nb_population = nb_population

        self.population = np.ndarray(nb_population, object)

        for i in range(nb_population):
            self.population[i] = Individual(NeuronNetwork(neuron_network_params[0], neuron_network_params[1], neuron_network_params[2], neuron_network_params[3], neuron_network_params[4]))

    def next_gen(self, mutation_rate):
        max = self.max_fitness()
        self.bread(max, mutation_rate)

    def max_fitness(self):
        max = self.population[0]
        for i in range(1, self.nb_population):
            if self.population[i].fitness > max.fitness:
                max = self.population[i]

        return max

    def bread(self, individual, mutation_rate):
        save = copy.deepcopy(individual)
        for p in range(self.nb_population):
            new = copy.deepcopy(save)
            for l in range(1, new.neuron_network.number_of_hidden_layers + 2):
                for n in range(new.neuron_network.layers[l].number_of_neurons):
                    for w in range(new.neuron_network.layers[l].neurons_weight[n].shape[0]):
                        percent = random.randrange(1, 100, 1)
                        if percent <= mutation_rate:
                            new.neuron_network.layers[l].neurons_weight[n][w] = 2 * np.random.random() - 1

            self.population[p] = new

