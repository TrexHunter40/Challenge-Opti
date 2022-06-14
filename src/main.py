import calculus as cal
import import_files as imp
import algos
import outpute as op

print("\n")


def run(num_instance, threshold):
    file = imp.import_file(num_instance)
    file_data = imp.import_file_data(file)

    nb_options = file_data[0]
    nb_cars = file_data[1]

    file.readline()
    file.readline()

    options = []
    cars = []

    imp.import_options(file, options, nb_options)

    file.readline()
    file.readline()

    imp.import_cars(file, cars, nb_cars)

    inst = cal.instance(nb_cars, nb_options, options, cars)

    #algos.randomselect(inst, threshold)

    algos.genetic(inst, 300, 0.2, threshold, num_instance)

def randrun(num_instance, threshold):
    file = imp.import_file(num_instance)
    file_data = imp.import_file_data(file)

    nb_options = file_data[0]
    nb_cars = file_data[1]

    file.readline()
    file.readline()

    options = []
    cars = []

    imp.import_options(file, options, nb_options)

    file.readline()
    file.readline()

    imp.import_cars(file, cars, nb_cars)

    inst = cal.instance(nb_cars, nb_options, options, cars)

    algos.randomselect(inst, threshold)

    #algos.genetic(inst, 200, 0.2, threshold, num_instance)

#randrun(8, 355)

run(6, 25)