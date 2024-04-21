#

from class_a import Die

''' can ignore this now was just testing the class
my_die = Die()
my_die.roll()
print(my_die)
my_die.roll()
print("New roll:", my_die.get_rolled_value())
my_die.roll()
print("Another roll:", my_die)
 '''


def main():
    die = Die()  
    while True:
        user_input = input("Roll the die? (yes/no): ")  
        if user_input.lower() == "yes":
            die.roll()  
            print(die)  
        elif user_input.lower() == "no":
            print("Exiting the program.")
            break  
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

main()

