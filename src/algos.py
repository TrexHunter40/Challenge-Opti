import numpy as np
import calculus as cal
import random as rd

def evaladd(inst, sequence, i, k):
    val = 0
    seq = sequence.copy()
    seq.append(inst.cars[k])
    for v in range(i):
        for o in range(inst.nboptions):
            excess = 0
            po = inst.options[o].weight
            for j in range(v, v+inst.options[o].P):
                if j < i:
                    excess += sequence[j].options[o]
            excess -= inst.options[o].N
            val += po * max(0, excess)
    return val

def algo1(inst):
    sequence = []
    for i in range(inst.nbcars):
        bestCar = -1
        bestVal = np.inf
        for k in range(inst.nbcars):
            if not(inst.cars[k] in sequence):
                val = evaladd(inst, sequence, i, k)
                if val < bestVal:
                    bestCar = k
                    bestVal = val
        print(i)
        sequence.append(inst.cars[k])
    return sequence


def randomgen(inst):
        cars2 = []
        temp = inst.cars.copy()
        listlen = inst.nbcars
        for k in range(inst.nbcars):
            r = rd.randint(0, listlen)
            cars2.append(temp.pop(r))
            listlen -= 1
        newInst = cal.instance(inst.nbcars, inst.nboptions, inst.options, cars2)
        return newInst

def randomselect(inst, threshold):
    costtobeat = inst.calcost()
    print("Cost to beat: " + costtobeat)
    while costtobeat > threshold:
        contendent = inst.randomgen()
        contendentcost = contendent.calcost()
        if contendentcost < costtobeat:
            costtobeat = contendentcost
            inst.cars = contendent.cars.copy()
    print("M O N K E found efFicIEncY: " + costtobeat)
