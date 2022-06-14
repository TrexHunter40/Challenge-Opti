import calculus as cal

# n -> numero de l'instance

def export(inst, n):
    f = open("res_"+str(n)+".txt", "w")
    f.write("EQUIPE monke\n")
    f.write("INSTANCE "+str(n)+"\n")
    for c in inst.cars:
        f.write(str(c.idcar) + " ")
    f.close()