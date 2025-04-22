import os
def write_to_file(file_name, content, is_new=False):
    if os.path.isfile(file_name) or is_new:
        with open(file_name, 'a') as file:
            if is_new:
                # Wider, cleaner header
                header = (
                "+--------------+-----------------+-----------------+-----------------+---------------+\n"
                "|                        D E D U C T I O N   L I S T                                 |\n"
                "+--------------+-----------------+-----------------+-----------------+---------------+\n"
                "| EmployeeID   |      SSS        |    PAG-IBIG     |   Phil-Health   |    BIR Tax    |\n"
                "+--------------+-----------------+-----------------+-----------------+---------------+\n"
            )
                file.write(header)
            file.write(content)
        print(f"Content successfully written to '{file_name}'.")
    else:
        print(f"Error: The file does not exist. Writing aborted.")

def deduction_Data():
    emp_id = input("Enter Employee ID: ")
    sss = input("Enter SSS Contribution: ")
    pagIbig = input("Enter Pag-IBIG Contribution: ")
    philHealth = input("Enter PhilHealth Contribution: ")
    bir_tax = input("Enter BIR Tax: ")
    return {"Employee_ID": emp_id, "SSS": sss, "PAG-IBIG": pagIbig, "Phil-Health": philHealth, "BIR Tax": bir_tax}

def confirm_and_save(file_name, content_dict):
    # Get the next employee ID

    # Display the entered data including Employee ID
    print("\n The data you entered:")
    print(f"Employee ID             : {content_dict['Employee_ID']}")
    print(f"SSS Contribution        : {content_dict['SSS']}")
    print(f"Pag-IBIG Contribution   : {content_dict['PAG-IBIG']}")
    print(f"PhilHealth Contribution : {content_dict['Phil-Health']}")
    print(f"BIR Tax                 : {content_dict['BIR Tax']}")

    # Ask for confirmation
    confirm = input("\nDo you want to save this information? (Y/N): ").strip().lower()

    if confirm == 'y':
        # Check if file is new
        is_new = not os.path.isfile(file_name) or os.path.getsize(file_name) == 0

        # Prepare the row
        content_str = f"| {content_dict['Employee_ID']:<12} | {content_dict['SSS']:<15} | {content_dict['PAG-IBIG']:<15} | {content_dict['Phil-Health']:^15} | {content_dict['BIR Tax']:<13} |\n"

        # Write to file
        write_to_file(file_name, content_str, is_new)
    else:
        print("\n🚫 Data not saved.")
