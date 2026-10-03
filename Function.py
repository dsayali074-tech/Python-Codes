#Question 6: Check Leap Year
#Concept: if-else, % modulus operator
#Input: One year
#Output: True or False

def is_leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap
year = int(input())
print(is_leap(year))