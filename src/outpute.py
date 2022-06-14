import calculus as cal

def export(inst):
    f = open("res_n.txt", "a")
    f.write("EQUIPE monke")
    f.write("INSTANCE n")
    for c in inst.cars:
        f.write(c.idcar + " ")
    f.close()