#

# Function to get students who took both prog1 and prog2
def get_students_who_took_prog1_and_prog2(prog1, prog2):
    return prog1.intersection(prog2)

# Function to get students who took either prog1 or prog2 or both
def get_students_who_took_prog1_or_prog2(prog1, prog2):
    return prog1.union(prog2)

# Function to get students who took prog1 but not prog2
def get_students_who_took_prog1_not_prog2(prog1, prog2):
    return prog1.difference(prog2)

# Function to get students who took prog2 but not prog1
def get_students_who_took_prog2_not_prog1(prog1, prog2):
    return prog2.difference(prog1)


prog1 = {'Student1', 'Student2', 'Student3'}
prog2 = {'Student3', 'Student4', 'Student5'}


students_who_took_both = get_students_who_took_prog1_and_prog2(prog1, prog2)
students_who_took_either = get_students_who_took_prog1_or_prog2(prog1, prog2)
students_who_took_prog1_only = get_students_who_took_prog1_not_prog2(prog1, prog2)
students_who_took_prog2_only = get_students_who_took_prog2_not_prog1(prog1, prog2)

#for testing purposes
print('Students who took both programs:', students_who_took_both)
print('Students who took either program:', students_who_took_either)
print('Students who took only the first program:', students_who_took_prog1_only)
print('Students who took only the second program:', students_who_took_prog2_only)
