
def create_file(filename):
    try:
        with open(filename,'w') as file:
            file.write("Hello this is dummy content for testing"+'\n')
            file.write("Just want to check if it overwrite or not!"+'\n')
            print("Congrates!!... file created successfully"+'\n')
    except IOError:
        print("Sorry!!......Something is fishy in write code...")

def append_file(filename, text):
    with open(filename,'a')as file:
        file.write(text)
        file.close()

def read_file(filename):
    try:
        with open(filename,'r')as file:
            print(file.read())
    except IOError:
        print("Sorry!!......Something is fishy in read code...")




filename = "hh.txt"

create_file(filename)
append_file(filename,"hello this is content i upload for the testing purpose of the append function")
read_file(filename)
