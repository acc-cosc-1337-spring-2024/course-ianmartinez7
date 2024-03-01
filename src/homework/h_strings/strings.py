#

from operator import index



def get_hamming_distance(dna1, dna2):
    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2 [i]:
            hamming_distance += 1
    return sum(c1 != c2 for c1, c2 in zip(dna1, dna2))

def get_dna_complement(dna):
    reversed_dna = dna[::-1]
    chac_swap = str.maketrans('ATCG', 'TAGC')
    complement_dna = reversed_dna.translate(chac_swap)
    return complement_dna

def menu ():
    print ("Homework 5 menu")
    print ("1-Hamming Distance")
    print ("2-DNA complement")
    print ("3-Exit")
    print (" ")

def get_menu_number():
    while True:
        number = int(input("Enter your choice 1, 2 or 3: "))
        if 1 <= number <= 3:
            return number
        else:
            print("Please pick a number between 1 - 3. ")

def exit_program():
    answer = input("Are you sure you want to exit the program? (yes/no): ")
    if answer in ("y", "yes"):
        return True
    elif answer in ("n", "no"):
        return False
                            




