import numpy as np
'''
Classes explaination:

car ---> idcar (int corresponding to its number in the instance file)
     |

'''
class car:
    def __init__(self, idcar, nboptions, options):
        self.idcar = idcar
        self.nbobtions = nboptions
        self.options = options

class option:
    def __init__(self, N, P, weight, idopt):
        self.N = N
        self.P = P
        self.weight = weight
        self.idopt = idopt

class instance:
    def __init__(self, nbcars, nboptions, options, cars):
        self.nbcars = nbcars
        self.nboptions = nboptions
        self.options = options
        self.cars = cars

    def calcost(instance):
        cost = 0
        for v in range(instance.cars):
            for o in range(instance.nboptions):
                excess = 0
                po = instance.options[o].weight
                for k in range(v, v+instance.options[o].P):
                    excess += instance.cars[k].options[o]
                excess -= instance.options[o].N
                cost += po * max(0, excess)

        return cost







        return cost
