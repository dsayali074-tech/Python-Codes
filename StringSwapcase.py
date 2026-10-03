#Question 13: Swap Case
#Concept: String, swapcase()
#Input: One string
#Output: Lowercase → Uppercase and Uppercase → Lowercase

def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)