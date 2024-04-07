#

from dictionary import add_inventory, remove_inventory_widget
from sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_not_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog2_not_prog1

def main_menu():
    inventory = {}

    while True:
        # Display the menu
        print("Inventory Menu")
        print("")
        print("1-Add or Update Item")
        print("2-Delete Item")
        print("3-Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            widget_name = input("Enter the widget name: ")
            quantity = int(input("Enter the quantity (add a negative number if you are updating inventory): "))
            print("")
            add_inventory(inventory, widget_name, quantity)
            print(f"Updated inventory: {inventory}")
            print("")
        elif choice == '2':
            widget_name = input("Enter the widget name to delete: ")
            result = remove_inventory_widget(inventory, widget_name)
            print(result)
            print(f"Updated inventory: {inventory}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")
#commenting out for working homework 7 menu
#main_menu()


def menu_homework_7():

    prog1 = {'Student1', 'Student2', 'Student3'}
    prog2 = {'Student3', 'Student4', 'Student5'}

    while True:
        print("\nInventory Menu")
        print("1-Students who took prog1 and prog2")
        print("2-Students who took prog2 only")
        print("3-Students who took prog1 not prog2")
        print("4-Students who took prog2 not prog1")
        print("5-Exit")
        print("")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(" ")
            print(get_students_who_took_prog1_and_prog2(prog1, prog2))
        elif choice == '2':
            print(" ")
            print(get_students_who_took_prog1_or_prog2(prog1, prog2))
        elif choice == '3':
            print(" ")
            print(get_students_who_took_prog1_not_prog2(prog1, prog2))
        elif choice == '4':
            print(" ")
            print(get_students_who_took_prog2_not_prog1(prog1, prog2))
        elif choice == '5':
            print(" ")
            print("Exiting the program.")
            break
        else:
            print(" ")
            print("Invalid choice. Please try again.")

menu_homework_7()