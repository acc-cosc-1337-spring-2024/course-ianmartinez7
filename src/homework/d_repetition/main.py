#

from ast import main
from multiprocessing.connection import answer_challenge
from repetition import get_factorial, menu, get_factorial_number, sum_odd_numbers, get_menu_number, get_son_number

       
from repetition import get_factorial, sum_odd_numbers, menu, get_menu_number, get_factorial_number, get_son_number, exit_program

def main():
    while True: 
        menu()
        choice = get_menu_number()  # Get the user's menu choice

        if choice == 1:
            user_number = get_factorial_number()  
            print(get_factorial(user_number)) 
        elif choice == 2:
            user_number = get_son_number()
            print(sum_odd_numbers(user_number))

        elif choice == 3:
            if exit_program():
                print("Exiting program. Goodbye!")
                break

        
        continue_program = input("Do you want to perform another operation? (yes/no): ")
        if continue_program not in ("y", "yes"):
            print("Exiting program. Goodbye....")
            break


main()
          


