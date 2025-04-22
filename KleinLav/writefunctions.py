import os
def write_to_file(file_name, content, is_new=False):
    if os.path.isfile(file_name) or is_new:
        with open(file_name, 'a') as file:
            if is_new:
                # Wider, cleaner header
                header = (
                "+--------------+-----------------+-----------------+---------+-----------+\n"
                "|                   E M P L O Y E E   L I S T                            |\n"
                "+--------------+-----------------+-----------------+---------+-----------+\n"
                "| EmployeeID   |   First Name    |    Last Name    |   Age   |  Gender   |\n"
                "+--------------+-----------------+-----------------+---------+-----------+\n"
            )
                file.write(header)
            file.write(content)
        print(f"Content successfully written to '{file_name}'.")
    else:
        print(f"Error: The file does not exist. Writing aborted.")

def employee_Data():
    fname = input("Enter First Name: ")
    lname = input("Enter Last Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    return {"First Name": fname, "Last Name": lname, "Age": age, "Gender": gender}

def confirm_and_save(file_name, content_dict):
    # Get the next employee ID
    emp_id = get_next_employee_id(file_name)

    # Display the entered data including Employee ID
    print("\n The data you entered:")
    print(f"Employee ID (auto): {emp_id}")
    print(f"First Name : {content_dict['First Name']}")
    print(f"Last Name  : {content_dict['Last Name']}")
    print(f"Age        : {content_dict['Age']}")
    print(f"Gender     : {content_dict['Gender']}")

    # Ask for confirmation
    confirm = input("\nDo you want to save this information? (Y/N): ").strip().lower()

    if confirm == 'y':
        # Check if file is new
        is_new = not os.path.isfile(file_name) or os.path.getsize(file_name) == 0

        # Prepare the row
        content_str = f"| {emp_id:^12} | {content_dict['First Name']:<15} | {content_dict['Last Name']:<15} | {content_dict['Age']:^7} | {content_dict['Gender']:<9} |\n"

        # Write to file
        write_to_file(file_name, content_str, is_new)
    else:
        print("\n🚫 Data not saved.")


def get_next_employee_id(file_name):
    """Reads the last employee ID from file and returns the next ID."""
    if not os.path.isfile(file_name) or os.path.getsize(file_name) == 0:
        return 1  # Start with 1 if file doesn't exist or is empty

    with open(file_name, 'r') as file:
        lines = file.readlines()
        ids = []
        for line in lines:
            if line.startswith("|"):
                parts = line.split("|")
                try:
                    emp_id = int(parts[1].strip())
                    ids.append(emp_id)
                except (ValueError, IndexError):
                    pass
        if ids:
            return max(ids) + 1
        else:
            return 1