import calculus as cal
import import_files as imp


print("\n")

file = imp.import_file()
file_data = imp.import_file_data(file)

nb_options = file_data[0]
nb_cars = file_data[1]

file.readline()
file.readline()

options = []
cars = []

imp.import_options(file, options)

file.readline()
file.readline()

imp.import_cars(file, cars)
