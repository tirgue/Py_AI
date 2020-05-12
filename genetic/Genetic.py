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
            for l in range(0, len(max)):
                if max[l].fitness < self.population[i].fitness:
                    max.insert(l, copy.deepcopy(self.population[i]))
                    insert = True
                    break

            if not insert:
                max.insert(len(max), copy.deepcopy(self.population[i]))

        for i in range(nb, self.nb_population):
            for j in range(len(max)):
                if self.population[i].fitness > max[j].fitness:
                    max.insert(j, copy.deepcopy(self.population[i]))
                    max.pop()

        return max

    def bread(self, individuals, mutation_rate):
        for p in range(self.nb_population):
            for l in range(1, self.population[p].neuron_network.number_of_hidden_layers + 2):
                for n in range(self.population[p].neuron_network.layers[l].number_of_neurons):
                    for w in range(self.population[p].neuron_network.layers[l].neurons_weight[n].shape[0]):
                        percent = random.randrange(1, 101, 1)
                        if percent <= mutation_rate:
                            self.population[p].neuron_network.layers[l].neurons_weight[n][w] = 2 * np.random.random() - 1
                        
                        else:
                            index = random.randrange(0,len(individuals),1)
                            self.population[p].neuron_network.layers[l].neurons_weight[n][w] = individuals[index].neuron_network.layers[l].neurons_weight[n][w]

                    percent = random.randrange(1, 100, 1)
                    if percent <= mutation_rate:
                        self.population[p].neuron_network.layers[l].biais = 2 * np.random.random() - 1
                    
                    else:
                        index = random.randrange(0,len(individuals),1)
                        self.population[p].neuron_network.layers[l].biais = individuals[index].neuron_network.layers[l].biais

            self.population[p].fitness = 0
