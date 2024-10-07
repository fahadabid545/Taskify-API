# def all_files():
# Importing OS Module to interact with OS(Operating System) to work on files.
import os
# Importing REGex Module to manipulate search pattern.
import re

# Defined a function to open file in it's associated program.
def default_file():
    file=input("Enter the exact file name with extension: ")
    os.startfile(file)        # os.startfile() -> starts file in its default program.

# Defined a function to read file content in terminal.
def file_in_terminal():
    a=input()
    with open (f"{a}", "r") as file:   # while using "with" we don't need to close file.
        for row in file:
            print(row)      # This will print each row in the file.

# Defined a function to fetch the all files similar to the user input.
def  find_file():
    file_name=input("File name\n").lower()
    reg_file_name=re.compile(re.escape(file_name),re.IGNORECASE)     #re.escape() Deals with special characters while re.IGNORECASE() make string case insensitive in this case user input i.e file_name. 
    search=os.path.expanduser("~")     #os.path.expanduser() allows os to search form the specific directory in this case from "home" 
    exact_file_name=[]        # Empty list to store the all file names similar to the user input.
    for path,_,files in os.walk(search):     #os.walk() starts searching for file from root in this case from "home" and then goes from all the paths to the file.
        if "appdata" in path.lower() or "program files"in path.lower():    # Condition is applied to avoid different apps and  program files named similar to the user input, so the user will be able to read only human readable files.
            continue              # jump over the files if it found any similar in program or app files.
        for file in files:        # iterate over all files
            if reg_file_name.search(file.lower()):       # Condition will check if the file name matches with the user input.
                exact_file_name.append(file)       # append files in the empty list.

    print("-----------------------")
    if exact_file_name:        # if there is a file in  list
        print("Files you might looking for")
        print("-----------------------")
        for files in exact_file_name:   # iterate over all files
            print(f"{files}")
    else:
        print("File not Found")
        print("-----------------------")

# defining the function to  find file path
def  find_file_path():
    file_name=input("File name\n").lower()     # getting user input
    reg_file_name=re.compile(re.escape(file_name),re.IGNORECASE)
    search=os.path.expanduser("~")
    for path,_,files in os.walk(search):      # iterating over paths from root to files
        if "appdata" in path.lower() or "program files"in path.lower():
            continue
        for file in files:
            if reg_file_name.search(file.lower()):
                print(f"Path found for file contains \"{file_name}\" in it's name")
                print("-----------------------------------------------------")
                print( os.path.join(path,file))      # Path of file/files similar to the user 

# find_file_path()

def  del_file():
    file_name=input("File name\n").lower()
    reg_file_name=re.compile(re.escape(file_name),re.IGNORECASE)
    search=os.path.expanduser("~")
    exact_file_path=[]
    exact_file_name=[]
    for path,_,files in os.walk(search):
        if "appdata" in path.lower() or "program files"in path.lower():
            continue
        for file in files:
            if reg_file_name.search(file.lower()):
                exact_file_path.append(os.path.join(path,file))
                exact_file_name.append(file)

    print("-----------------------")
    if len(exact_file_name)>=1:
        print("Files you might looking for along with their paths")
        print("-----------------------")
        for file, path in zip(exact_file_name, exact_file_path):
            print("File you might looking for along with it's path")
            print(f"FILE FOUND,NAMED AS: {file} have path: \n{path}")
    else:
        print("File not Found")
        print("-----------------------")
        return
    while True:
        ask_user=input("Enter exact file path you want to delete or enter 'exit' to quit. \n").strip()
        if ask_user in exact_file_path:
            try:
                os.remove(ask_user)
                print("File Deleted")
                break
            except Exception as e:
                print(f"Error: {e}")
        elif ask_user=="exit":
            print("Existing without deleting")
            break
        else: 
            print("No Matching file found, please try again")
                
del_file()