# Release Notes

"""
Release Notes 1.001

- Update directory and sub-directory structures.
- Added feature to generate Python or HTML project folder.
"""

# Modules

import os
import datetime

# Variables

dateformat1 = datetime.datetime.today().strftime("%Y%m%d")
user = os.getlogin()

def project_python():

    # Variables

    path1 = f"C:/Users/{user}/desktop/"
    dir_python = f"python_project_{dateformat1}"
    path2 = path1 + dir_python
    file_py = f"untitled_{dateformat1}_1.000.py"

    # Create a main directory.

    os.mkdir(path1 + dir_python)

    # Change directory.

    os.chdir(path2)

    # Create sub-directories.

    os.mkdir("db")
    os.mkdir("media")
    os.mkdir("media/icons")
    os.mkdir("media/images")
    os.mkdir("media/sounds")
    os.mkdir("media/ui")
    os.mkdir("logs")
    os.mkdir("scripts")

    # Create a .py file.

    open(file_py, "w", ).write("")

    # Open the project folder in Windows Explorer.

    os.startfile(path2)

def project_html():

    # Variables

    path1 = f"C:/Users/{user}/desktop/"
    dir_html = f"html_project_{dateformat1}"
    path2 = path1 + dir_html
    file1_html = "index.html"

    # Create a directory.

    os.mkdir(path1 + dir_html)

    # Change main directory.

    os.chdir(path2)

    # Create sub-directories.

    os.mkdir("media")
    os.mkdir("media/images")
    os.mkdir("styles")
    os.mkdir("scripts")

    # Create a .html file.

    open(file1_html, "w", ).write("")

    # Open the project folder in Windows Explorer.

    os.startfile(path2)

def menu():

    print("Which project would you like to generate?")
    print("\n1. Python")
    print("2. HTML")

    choice = input("\nEnter an option: ")

    if choice == "1":
        project_python()
    elif choice == "2":
        project_html()
    else:
        print("Invalid Option. Please try again.")
        menu()
menu()
