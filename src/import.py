import os

def string_extract(str) :
    res = ''

    for i in str :
        if i.isdigit():
            res += i

    res = int(res)

    return res



def import_file():

    cur_path = os.path.dirname(__file__)
    file_path = cur_path + "/Instances/cs1.txt"

    file = open(file_path, "rt")
    #print(file.read())

    line1 = file.readline()
    line2 = file.readline()

    print(line1+line2)

print("\n")

print(string_extract("ABc 36"))
#import_file()