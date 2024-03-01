#

from strings import menu, get_hamming_distance, get_dna_complement, get_menu_number, exit_program


def main():
    while True: 
        menu()
        choice = get_menu_number()# Get the user's menu choice

        if choice == 1:
            print("This option will calculate hamming distance between two DNA string")
            user_sting1 = input('Input first DNA string ')
            user_string2 = input("Input second DNA string ")
            print(get_hamming_distance(user_sting1, user_string2))

             
        elif choice == 2:
            print("This option will calculate the reverse complement of a DNA string")
            user_sting3 = input('Input DNA string. ')
            print(get_dna_complement(user_sting3))

        elif choice == 3:
            if exit_program():
                print("Exiting program. Goodbye!")
                break

        
        continue_program = input("Do you want to perform another operation? (yes/no): ")
        if continue_program not in ("y", "yes"):
            print("Exiting program. Goodbye....")
            break

main()