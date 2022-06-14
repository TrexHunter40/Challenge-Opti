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
            r = rd.randint(0, listlen-1)
            cars2.append(temp.pop(r))
            listlen -= 1
        newInst = cal.instance(inst.nbcars, inst.nboptions, inst.options, cars2)
        return newInst

def randomselect(inst, threshold):
    costtobeat = inst.calcost()
    
    while costtobeat > threshold :
        print("Cost to beat: " + str(costtobeat))

        contendent = randomgen(inst)
        contendentcost = contendent.calcost()

        if contendentcost < costtobeat:
            costtobeat = contendentcost
            inst.cars = contendent.cars.copy()
        
    print("M O N K E found efFicIEncY: " + str(costtobeat))


def genetic(inst, pop, perm_chance) :
    gen = 1
    cost = inst.calcost()
    genetic_recurr(inst, cost, gen, pop, perm_chance)


def genetic_recurr(curr_inst, curr_cost, gen, pop, perm_chance) :

    print("Generation "+str(gen))
    print("Cost : "+str(curr_cost))
    print("\n")

    min_cost = curr_cost
    last_inst = cal.instance(curr_inst.nbcars, curr_inst.nboptions, curr_inst.options, curr_inst.cars.copy())
    best_inst = cal.instance(last_inst.nbcars, last_inst.nboptions, last_inst.options, last_inst.cars.copy())

    for i in range(pop) :
        curr_inst = cal.instance(last_inst.nbcars, last_inst.nboptions, last_inst.options, last_inst.cars.copy())

        #neighbourg_perm(curr_inst, 0.2)
        for i in range(curr_inst.nbcars-1) :
            if rd.random() < perm_chance :
                curr_inst.cars[i], curr_inst.cars[i+1] = curr_inst.cars[i+1], curr_inst.cars[i]
        cost = curr_inst.calcost()
        #print(cost)

        if cost <= min_cost :
            min_cost = cost
            best_inst = cal.instance(curr_inst.nbcars, curr_inst.nboptions, curr_inst.options, curr_inst.cars.copy())

    genetic_recurr(best_inst, min_cost, gen+1, pop, perm_chance)


def neighbourg_perm(inst, perm_chance) :
    pass
    