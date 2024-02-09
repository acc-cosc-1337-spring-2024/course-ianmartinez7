

def get_options_ratio(option, total):
    if total == 0:
        raise "Total cannot b zero"
    return option / total

def get_faculty_rating(ratio):
    if ratio >= .9 and ratio < 1:
        return "Excellent"
    if ratio >= .8 and ratio < .9:
        return "Very Good"
    if ratio >= .7 and ratio < .8:
        return "Good"
    if ratio >= .6 and ratio < .7:
        return "Needs Improvement"
    if ratio < .59 and ratio >= 0:
        return "Unacceptable"
    elif ratio > 1:
        return "Ratings are between 1 - 0"
      # If ratio is not between 0 and 1
      #check spelling when running the test case lol

  