import numpy as np
import random as rd

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

    def calcost(inst):
        cost = 0
        for v in range(inst.nbcars):
            for o in range(inst.nboptions):
                excess = 0
                po = inst.options[o].weight
                for k in range(v, v+inst.options[o].P):
                    if k < inst.nbcars:
                        excess += inst.cars[k].options[o]
                excess -= inst.options[o].N
                cost += po * max(0, excess)

        return cost

    def randomgen(inst):
        cars2 = []
        temp = inst.cars.copy()
        listlen = inst.nbcars
        for k in range(inst.nbcars):
            r = rd.randint(0, listlen)
            cars2.append(temp.pop(r))
            listlen -= 1
        newinst = instance(inst.nbcars, inst.nboptions, inst.options, cars2)
        return newinst

    def randomselect(inst, threshold):
        costtobeat = inst.calcost()
        printf("Cost to beat: " + costtobeat)
        while costtobeat > threshold:
            contendent = inst.randomgen()
            contendentcost = contendent.calcost()
            if contendentcost < costtobeat:
                costtobeat = contendentcost
                inst.cars = contendent.cars.copy()
        print("M O N K E found efFicIEncY: " + costtobeat)







'''
c0 = car(0, [1, 1])
c1 = car(1, [0, 1])


o0 = option(1, 2, 3, "option1")
o1 = option(1, 4, 5, "option2")

inst = instance(2, 2, [o0, o1], [c0, c1])

cost = inst.calcost()
print(cost)
'''

