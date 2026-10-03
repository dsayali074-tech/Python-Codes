#Question 5: Print Square of Numbers
#Concept: for loop, range(), square i * i
#Input: One integer n
#Output: 0 to n-1 no square
#Example :n = 5
#        0 × 0 = 0
#        1 × 1 = 1
#        2 × 2 = 4
#        3 × 3 = 9
#        4 × 4 = 16

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i * i)
