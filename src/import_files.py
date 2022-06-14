import os
import re

def string_extract_int(str) :
    res = ''

    for i in str :
        if i.isdigit():
            res += i

    res = int(res)

    return res

def string_extract_tab(str) :
    num_tab = list(map(int, re.findall('\d+', str)))

    print(num_tab)
    return num_tab


def import_options(file) :
    curr_line = file.readline()
    id = curr_line[-6:]    
    values_str = curr_line[:-7]
    option_values = string_extract_tab(values_str)

    print(id)
    #print(option_values)

def import_cars(file) :
    curr_line = file.readline()
    car_values = string_extract_tab(curr_line)



def import_file():

    cur_path = os.path.dirname(__file__)
    file_path = cur_path + "/Instances/cs1.txt"

    file = open(file_path, "rt")
    #print(file.read())

    line1 = file.readline()
    line2 = file.readline()

    nb_options = string_extract_int(line1)
    nb_cars = string_extract_int(line2)

    file.readline()
    file.readline()

    import_options(file)

    #print(nb_options)
    #print(nb_cars)

print("\n")

import_file()