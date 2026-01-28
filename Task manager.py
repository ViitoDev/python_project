import os

tasks = []

def main_menu():
    input("Press any key to return to the menu.")
    main()

def title(text):
    os.system("cls")
    line = '*' * (len(text) + 4)
    print(line)
    print(text)
    print(line)
    print()

def invalid_option():
    print("Invalid option!\n")
    main_menu()

def show_options():
    print("1. Add task")
    print("2. Show tasks")
    print("3. Remove tasks")
    print("4. Exit program")

def add_tasks():
    title("Add task")
    add_task = input("Enter a new task: \n")
    tasks.append(add_task)
    print(f"The task {add_task} was successfully added.")
    main_menu()

def show_tasks():
    title("Show tasks")
    counter = 1
    for task in tasks:
        print(f"[{counter}]{task}")
        counter += 1
    main_menu()

def remove_task():
    remove_option = int(input("Enter the number you want to delete: \n")) - 1
    del tasks [remove_option]
    main_menu()

def exit_program():
    os.system("cls")

def choose_option():
    try:
        option = int(input("Enter your option: \n"))
        if option == 1:
            add_tasks()
        elif option == 2:
            show_tasks()
        elif option == 3:
            remove_task()
        elif option == 4:
            exit_program()
        else:
            invalid_option()
    except:
        invalid_option()
            

def main():
    os.system("cls")
    show_options()
    choose_option()

if __name__ == "__main__":
    main()