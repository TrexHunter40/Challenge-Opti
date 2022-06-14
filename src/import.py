import os

def import_file():

    cur_path = os.path.dirname(__file__)
    file_path = cur_path + "/Instances/cs1.txt"

    file = open(file_path, "rt")
    print(file.read())

    

import_file()