#

from class_a import Die

#### test case to make sure code works
my_die = Die()
my_die.roll()
print(my_die)
my_die.roll()
print("New roll:", my_die.get_rolled_value())
my_die.roll()
print("Another roll:", my_die)
### end of the test case
