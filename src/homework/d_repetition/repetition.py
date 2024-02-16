#math
def get_factorial(num):
    factorial = 1

    if num < 0:
        return "factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
    return factorial
#math
def sum_odd_numbers(num):
    sum = 0
    cnt = 1
    while cnt <= num:
        if cnt % 2 == 1:
            sum += cnt
        cnt += 1
        
    return sum

#main menu function 
def menu ():
    print ("Homework 3 Menu")
    print ("1-Factorial")
    print ("2-sum odd numbers")
    print ("3-Exit")
    print (" ") 

#menu options pick
def get_menu_number():
    while True:
        number = int(input("Enter your choice 1, 2 or 3: "))
        if 1 <= number <= 3:
            return number
        else:
            print("Please pick a number between 1 - 3. ")



#if get_menu_number == 1
def get_factorial_number():
    while True:  # Start an infinite loop.
            number = int(input("Enter a number between 1 and 10: ")) 
            if 1 <= number <= 10:  
                return number  
            else:
                print("The number must be between 1 and 10. Try again.") 




#function for getting number if get_menu_number == 2
def get_son_number():
    while True:
        number = int(input("Enter a number between 1 - 100. "))
        if 1 <= number <= 100:
            return number
        else:
            print("Please pick a number between 1 - 100.")

# if get_menu_number = 3
def exit_program():
    answer = input("Are you sure you want to exit the program? (yes/no): ")
    if answer in ("y", "yes"):
        return True
    elif answer in ("n", "no"):
        return False  
