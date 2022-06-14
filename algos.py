import numpy as np
import calculus as cal

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
        bestVeh = -1
        bestVal = np.inf
        for k in range(inst.nbcars):
            if not(inst.cars[k] in sequence):
                val = evaladd(k)
                if val < bestVal:
                    bestVeh = k
                    bestVal = val
        sequence.append(inst.cars[k])
    return sequence