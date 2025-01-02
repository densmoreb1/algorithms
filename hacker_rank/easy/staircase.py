# https://www.hackerrank.com/challenges/staircase/problem
# print a staircase of n stairs
#
##
###
####

def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * (i))
