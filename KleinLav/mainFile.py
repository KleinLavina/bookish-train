import callfunctions as mine
import writefunctions as write
import deductionfunc as ded
import os
# Clear screen

# Display menu options in a table format


while True:
    mine.cls()
    print("=" * 50)
    print("{:<10} {:<20}".format("Command", "Description"))
    print("=" * 50)
    print("{:<10} {:<20}".format("C", "CREATE A TEXT FILE"))
    print("{:<10} {:<20}".format("W", "WRITE INTO A TEXT FILE"))
    print("{:<10} {:<20}".format("R", "READ CONTENTS"))
    print("{:<10} {:<20}".format("D", "DELETE A TEXT FILE"))
    print("{:<10} {:<20}".format("E", "Exit Program"))
    print("=" * 50)
    
    command = input("\nEnter Command: ").lower()
   

    if command == "c":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "CREATE A FILE TO: ")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)
        comms = input("Enter Command: ").lower()
        if comms == "e":
            mine.create_file("employee.txt")
        elif comms == "d":
            mine.create_file("deductions.txt")
        else:
            print("Invalid Command!! Please re-enter command")
            comms = input("Enter Command: ").lower()


    elif command == "w":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "WRITE A TEXT FILE TO: ")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)
        comms = input("Enter Command: ").lower()

        if comms == "e":
            file_name = "employee.txt"
            
            is_new = not os.path.isfile(file_name) or os.path.getsize(file_name) == 0

            # Get employee data
            content = write.employee_Data()

            # Confirmation before writing
            write.confirm_and_save(file_name, content)

        elif comms == "d":
            file_name = "deductions.txt"
            
            is_new = not os.path.isfile(file_name) or os.path.getsize(file_name) == 0

            # Get deduction data
            content = ded.deduction_Data()

            # Confirmation before writing
            ded.confirm_and_save(file_name, content)
           
        else:
            print("Invalid Command: ")
            comms = input("Enter Command: ").lower()

    elif command == "r":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "READ A TEXT FILE INTO ?")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)
        comms = input("Enter Command: ").lower()
        if comms == "e":
            mine.cls()
            print("=" * 50)
            file_content = mine.read_file('employee.txt')
            print("\nFile Content:\n" + "-" * 50)
            print(file_content)
            print("-" * 50)

        elif comms == "d":
            mine.cls()
            print("=" * 50)
            file_content = mine.read_file('deductions.txt')
            print("\nFile Content:\n" + "-" * 50)
            print(file_content)
            print("-" * 50)

        else:
            print("Invalid Command: ")
            comms = input("Enter Command: ").lower()
      

    elif command == "d":
        mine.cls()
        print("=" * 50)
        print(" " * 10, "DELETE a File to ")
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Employee"))
        print("{:<10} {:<20}".format("D", "Deduction"))
        print("=" * 50)
        file_name_del = mine.confirmDelete()
        confirm = input(f"Proceed to Delete a '{file_name_del}' file text : (y/n)").lower()
        if confirm == "y":
            mine.cls()
            print("=" * 50)
            print(" " * 10, "Read a File to ")
            print("=" * 50) 
            mine.delete_file(file_name_del)
        elif confirm == "n":
            print("File has not deleted")
        else:
            print("Invalid Command")

    elif command == "e":
        mine.cls()
        print("=" * 50)
        print("{:<10} {:<20}".format("E", "Exiting a Program"))
        print("=" * 50)
        exit_confirm = input("\nAre u sure u want to exit? (y/n): ").lower()
        if exit_confirm != 'n':
            print("\nExiting the program. Goodbye!")
            break

        

    else:
        print("Invalid command. Please enter a valid command.")

    # Ask if the user wants to continue or exit
    continue_prompt = input("\nDo you want to continue? (y/n): ").lower()
    if continue_prompt != 'y':
        print("\nExiting the program. Goodbye!")
        break
