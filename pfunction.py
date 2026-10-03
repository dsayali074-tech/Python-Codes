# Question 7: Print Consecutive Numbers
# Concept: for loop + print(end="")
# Input: One integer n
# Output: 1 to n numbers without spaces

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')
    
