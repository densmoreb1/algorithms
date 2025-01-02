# https://www.hackerrank.com/challenges/the-birthday-bar/problem
# find combinations if they add to d
# combinations of m length
# s is the arrary

def birthday(s, d, m):
    c = 0
    for i in range(len(s) - m + 1):
        print(s[i:i + m])
        print(i + m)
        if sum(s[i:i + m]) == d:
            c += 1
    return c
