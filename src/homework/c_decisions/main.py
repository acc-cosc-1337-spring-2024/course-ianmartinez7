#

from decisions import get_options_ratio, get_faculty_rating

ratio = get_options_ratio(10,20)
print (ratio)

rating = get_faculty_rating(ratio)
print(rating)
# can compare what returns for rating vs input_rating and see if you get the same rating
options = input("What is the number of your options? ")
total = input("What is the total? ")

input_rating = get_faculty_rating(int(options) / int(total))
print(input_rating)

