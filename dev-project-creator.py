# Modules

import os
import datetime

# Variables

dateformat1 = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
user = os.getlogin()
path = fr"C:/Users/{user}/desktop/"
py_directory = fr"py-project-{dateformat1}"
html_directory = fr"html-project-{dateformat1}"

def py_project():

    # Create project directory

    os.mkdir(os.path.join(path, py_directory))

    # Change directory

    os.chdir(os.path.join(path, py_directory))

    # Create sub-directories

    os.mkdir('build')
    os.mkdir('db')
    os.mkdir('scripts')
    os.mkdir('UI')
    
    # Create Virtual Environment
    
    os.system(r'python -m venv venv')

    # Create files

    with open("script.py", "w", ) as file1:
        file1.write("")

    with open("requirements.txt", "w", ) as file2:
        file2.write("")

    with open("config.ini", "w", ) as file3:
        file3.write("[DEFAULT]")

def html_project():

    # Create project directory

    os.mkdir(os.path.join(path, html_directory))

    # Change directory

    os.chdir(os.path.join(path, html_directory))

    # Create sub-directories

    os.mkdir("media")
    os.mkdir("media/images")
    os.mkdir("styles")
    os.mkdir("scripts")

    # Create a .html file.

    with open("index.html", "w", ) as file1:
        file1.write("")

def menu():

    print("Select an option to begin project generation:\n")
    print("1. Python")
    print("2. HTML")

    choice = input("\nEnter an option: ")

    if choice == "1":
        print("\nCreating Python Project ..")
        py_project()
        input("\nComplete! Press any Key to exit ..")
        os.startfile(os.path.join(path, py_directory))
    elif choice == "2":
        print("\nCreating HTML Project ..")
        html_project()
        input("\nComplete! Press any Key to exit ..")
        os.startfile(os.path.join(path, html_directory))
    else:
        print("Invalid Option. Please try again.")
        menu()
menu()
