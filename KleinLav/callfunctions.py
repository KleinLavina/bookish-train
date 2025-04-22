import os

# 1. Function to clear the screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")

# 2. Function to create an empty file
def create_file(file_name):
    try:
        with open(file_name, 'x') as file:
            print(f"File '{file_name}' has been created.")
    except FileExistsError:
        print(f"Error: The file '{file_name}' already exists.")

# 3. Function to write content to an existing file


# 4. Function to read the content of a file
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_name}' does not exist."

# 5. Function to delete a file
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' has been deleted.")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")


def confirmDelete():
    comms = input("Enter Command: ").lower()
    if comms == "e":
        file_name_del = 'employee.txt'
    elif comms == "d":
        file_name_del = 'deductions.txt'
    else:
        print("Invalid Command: ")
    return file_name_del