import os, sys

def startProgram():
    print("\nHello there! Welcome to file manager")
    print("\nPress 1 to view and update files")
    print("Press 2 to create a new file")
    print("Press 3 to remove a file")
    print("Press 4 to exit out of program")
    option = input("> ")
    if option == "1":
        fileManager()
    elif option == "2":
        create_file()
    elif option == "3":
        remove_file()
    elif option == "4":
        sys.exit
    else:
        print("\nInvalid input")
        startProgram()

def fileManager():
    print("Here is a list of the files")
    print(" ")
    files = os.listdir("Place file path here") #rename filepath to your current machine
    for file in files:
        if not "filemanager.py" in file:
            print(file)
    print("\nType in filename to manage file or press H to go back to home page")
    option = input("> ")
    if option == "h" or option == "H":
        startProgram()
    else:
        if option in files:
            manage_chosen_file(option)
        else:
            print("Filename does not exist")
            fileManager()

def manage_chosen_file(file):
    print("\nPress 1 to view contents of " + file)
    print("Press 2 to overwrite contents of " + file)
    print("Press 3 to append to " + file)
    print("Press 4 to empty contents of " + file)
    print("Press B to go back to filemanager")
    print("Press H to go back to home page")
    option_manage = input("> ").lower()
    if option_manage == "h":
        startProgram()
    elif option_manage == "b":
        fileManager()
    elif option_manage == "1":
        read_file(file)
    elif option_manage == "2":
        overwite_file(file)
    elif option_manage == "3":
        append_file(file)
    elif option_manage == "4":
        empty_file(file)


def read_file(inputfile):
    with open(inputfile) as file:
        print("\nHere are the contents of " + inputfile)
        file_read = file.read()
        print(file_read)
        file.close()
    file_options_goback(inputfile)

def overwite_file(inputfile):
    print("\nWhat would you like to overwrite to " + inputfile + "?")
    print("Input text or press B to go back")
    overwrite = input("> ")
    if overwrite == "b" or overwrite == "B":
        manage_chosen_file(inputfile)
    with open(inputfile, "w") as file:
        file.write(overwrite)
        print("\nSuccessfully written to " + inputfile)
        file.close()
    file_options_goback(inputfile)

def append_file(inputfile):
    print("\nWhat would you like to append to " + inputfile + "?")
    print("Input text or press B to go back")
    append = input("> ")
    if append == "b" or append == "B":
        manage_chosen_file(inputfile)
    with open(inputfile, "a") as file:
        file.write("\n" + append)
        print("\nSuccessfully appended to " + inputfile)
        file.close()
    file_options_goback(inputfile)

def empty_file(inputfile):
    print("\nAre you sure you want to empty contents of " + inputfile + "?")
    print("Y/N")
    empty = input("> ").lower()
    if empty == "y":
        with open(inputfile, "w") as file:
            file.truncate()
            print("\nSuccessully emptied " + inputfile)
            file.close()
        file_options_goback(inputfile)
    elif empty == "n":
        manage_chosen_file(inputfile)

def file_options_goback(inputfile):
    print("\n What would you like to do now?")
    print("Press B to do something else with " + inputfile)
    print("Press H to go back home")
    option = input("> ")
    if option == "b":
        manage_chosen_file(inputfile)
    elif option == "h":
        startProgram()
    else:
        print("Invalid input")
        file_options_goback(inputfile)

def create_file():
    files = os.listdir("Place file path here")
    print("\nInput name of file you want to create")
    print("Or press B to go back")
    file_create = input("> ")
    if file_create == "b" or file_create == "B":
        startProgram()
    elif file_create in files:
        print(file_create + " already exists")
        startProgram()
    else:
        new_file = open(file_create, "w")
        print("Successfully created file " + file_create)
    startProgram()

def remove_file():
    print("\nWhich file would you like to remove?")
    files = os.listdir("Place file path here") #rename filepath to your current machine
    for file in files:
        if not "filemanager.py" in file:
            print(file)
    print("\nType in filename to remove file or press H to go back to home page")
    option = input("> ")
    if option == "h" or option == "H":
        startProgram()
    else:
        if option in files:
            print("\nAre you are you would like to remove the file " + option + "?")
            print("Y/N")
            delete = input("> ").lower()
            if delete == "y":
                os.remove(option)
                print("Successfully removed file " + option)
                startProgram()
            elif delete == "n":
                startProgram()
            else:
                print("Invalid input")
                startProgram()
        else:
            print("Filename " + option + "does not exist")
            startProgram()

def exit_program():
    print("Thank you and have a nice day!")
    sys.exit


startProgram()
