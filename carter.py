employee = []

def add_employee_info():
    global employee
    name = str(input("Please enter the employee's name: "))
    age = int(input("Please enter the employee's age: "))
    while age<18:
        print("Are you a minor? Wait for some years later.")
        age = int(input("Please enter the employee's age: "))
    position = str(input("Please enter the employee's current position: "))
    employee_info = {
        "name": name,
        "age": age,
        "position": position
    }
    employee.append(employee_info)
    print(employee)


def action_change():
    while True:
            change_info = input("Would you like to change anything? Yes or no? ")
            if change_info == "Yes":
                option = input("Please choose between these options: name, age, position or status.Your option: ")
                if option == "name":
                    new_name = str(input("Please enter the employee's new name: "))
                    new_name1 = employee.replace(name, new_name)
                    employee.append(new_name1)
                elif option == "position":
                    new_position = str(input("Please enter the employee's current position: "))
                    employee.replace(position, new_position)
                elif option == "status":
                    print("The employee had resigned or been fired.")
                else:
                    print("That option does not exist. Try again.")
                    option = input("Please choose between these options: name, age, position or status.Your option: ")
            elif change_info == "No":
                break

def change_info():
    global name
    global position
    employee_name = str(input("Please enter the employee's name: "))

    for x in employee:
        if x.name == employee_name:
            action_change()
            break
            

    
def main():
    while True:
        print("\n Chào mừng đến với công ty. \n")
        print("1.Add employee information")
        print("2.Change something about the information")
        print("3.exit")
        choice = input("Please choose your option from 1 to 3: ")
        if choice == '1':
            add_employee_info()
        elif choice == '2':
            change_info()
        elif choice == '3':
            exit()
        else:
            print("That option does not exist. Please try again.")
            choice = input("Please choose your option from 1 to 3: ")
main()
































