#Question 15: Print Full Name
# Concept: Function, String, print()
# Input: First name and Last name
# Output: "Hello Firstname Lastname! You just delved into python.

def print_full_name(first, last):
    print("Hello", first, last + "! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)