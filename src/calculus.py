
class car:
    def __init__(self, idcar, options):
        self.idcar = idcar
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

    def calcost(self):
        cost = 0
        for v in range(self.nbcars):
            for o in range(self.nboptions):
                excess = 0
                po = self.options[o].weight
                for k in range(v, v+self.options[o].P):
                    if k < self.nbcars:
                        excess += self.cars[k].options[o]
                excess -= self.options[o].N
                cost += po * max(0, excess)

        return cost

    def max_weight(self):
        max = 0
        for option in self.options :
            if option.weight > max :
                max = option.weight
        return max

    







'''
c0 = car(0, [1, 1])
c1 = car(1, [0, 1])


o0 = option(1, 2, 3, "option1")
o1 = option(1, 4, 5, "option2")

inst = instance(2, 2, [o0, o1], [c0, c1])

cost = inst.calcost()
print(cost)
'''

