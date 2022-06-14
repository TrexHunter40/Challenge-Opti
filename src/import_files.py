import os
import re
import calculus as cal

def string_extract_int(str) :
    res = ''

    for i in str :
        if (i.isdigit()):
            res += i
    res = int(res)

    return res

def string_extract_tab(str) :
    num_tab = list(map(int, re.findall('\d+', str)))

    #print(num_tab)
    return num_tab


def import_file():
    cur_path = os.path.dirname(__file__)
    file_path = cur_path + "/Instances/cs1.txt"
    return open(file_path, "rt")


def import_file_data(file) :

    line1 = file.readline()
    line2 = file.readline()

    nb_options = string_extract_int(line1)
    nb_cars = string_extract_int(line2)

    return [nb_options, nb_cars]


def import_options(file, options, nb_options) :
    for  i in  range(nb_options) :
        curr_line = file.readline()
        id = curr_line[-6:]    
        values_str = curr_line[:-7]
        option_values = string_extract_tab(values_str)

        options.append(cal.option(option_values[0], option_values[1], option_values[2], id))


def import_cars(file, cars, nb_cars) :
     for i in range(nb_cars) :
        curr_line = file.readline()
        car_values = string_extract_tab(curr_line)

        #print(car_values)

        cars.append(cal.car(car_values[0], car_values[1:]))

"""
print("\n")
file = import_file()
file_data = import_file_data(file)"""