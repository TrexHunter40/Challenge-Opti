import calculus as cal
import os

# n -> numero de l'instance

def export(inst, n):
    cur_path = os.path.dirname(__file__)
    f = open(cur_path + "/Instances/res_"+str(n)+".txt", "w")
    f.write("EQUIPE monke\n")
    f.write("INSTANCE "+str(n)+"\n")
    for c in inst.cars:
        f.write(str(c.idcar) + " ")
    f.close()