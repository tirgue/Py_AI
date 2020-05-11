from .Individual import *
import numpy as np
import copy
import random

class Genetic(object):
    
    def __init__(self, nb_population, neuron_network_params):
        self.nb_population = nb_population

        self.population = np.ndarray(nb_population, object)

        for i in range(nb_population):
            self.population[i] = Individual(NeuronNetwork(neuron_network_params[0], neuron_network_params[1], neuron_network_params[2], neuron_network_params[3]))

    def next_gen(self, mutation_rate, nb_parent):
        max = self.max_fitness(nb_parent)
        self.bread(max, mutation_rate)

    def max_fitness(self, nb):
        max = [copy.deepcopy(self.population[0])]
        for i in range(1, nb):
            insert = False
            for l in range(len(max) - 1, -1, -1):
                if max[l].fitness < self.population[i].fitness:
                    max.insert(l + 1, copy.deepcopy(self.population[i]))
                    insert = True
                    break

            if not insert:
                max.insert(0, copy.deepcopy(self.population[i]))

        for i in range(1, self.nb_population):
            if self.population[i].fitness > max[nb-1].fitness:
                max.append(copy.deepcopy(self.population[i]))
                max.pop(0)

        return max

    def bread(self, individuals, mutation_rate):
        for p in range(self.nb_population):
            for l in range(1, self.population[p].neuron_network.number_of_hidden_layers + 2):
                for n in range(self.population[p].neuron_network.layers[l].number_of_neurons):
                    for w in range(self.population[p].neuron_network.layers[l].neurons_weight[n].shape[0]):
                        percent = random.randrange(1, 100, 1)
                        if percent <= mutation_rate:
                            self.population[p].neuron_network.layers[l].neurons_weight[n][w] = 2 * np.random.random() - 1
                        
                        else:
                            index = random.randrange(0,len(individuals)-1,1)
                            self.population[p].neuron_network.layers[l].neurons_weight[n][w] = individuals[index].neuron_network.layers[l].neurons_weight[n][w]

                    percent = random.randrange(1, 100, 1)
                    if percent <= mutation_rate:
                        self.population[p].neuron_network.layers[l].biais = 2 * np.random.random() - 1
                    
                    else:
                        index = random.randrange(0,len(individuals)-1,1)
                        self.population[p].neuron_network.layers[l].biais = individuals[index].neuron_network.layers[l].biais

            self.population[p].fitness = 0
