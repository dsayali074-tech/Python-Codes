# Question 8: Find Runner-Up Score
# Concept: List, max(), sorting / second highest value
# Input: Scores  list
# Output: Second highest score

if __name__ == '__main__':
    n = int(input())
scores = list(map(int,input().split()))
scores = list(set (scores))
scores.sort ()
print(scores[-2])
