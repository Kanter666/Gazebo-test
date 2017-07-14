import os
import numpy


def create_file(location_name, context):
    numpy.savetxt(location_name, [context], delimiter=" ", fmt="%s")

def main():
    print("running model creator")
    model = "testing_model"
    directory = "../Models/"+model
    if not os.path.exists(directory):
        os.makedirs(directory)

    file = directory+"/model.sdf"
    create_file(file, "some string")

if __name__ == "__main__": main()
