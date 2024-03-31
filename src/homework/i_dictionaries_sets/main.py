#

from dictionary import add_inventory, remove_inventory_widget

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

main_menu()