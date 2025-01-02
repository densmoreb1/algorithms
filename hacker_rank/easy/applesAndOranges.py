# https://www.hackerrank.com/challenges/apple-and-orange/problem
# s start point of the house
# t end point of the house
# a where the apple tree is
# b where the orange tree is
# apples array of how far apples fall
# oranges array of how far the oranges fall

def countApplesAndOranges(s, t, a, b, apples, oranges):
    steves_house = list(range(s, t + 1))
    land_apple = 0
    land_orange = 0
    for apple in apples:
        if a + apple >= s and a + apple <= t:
            land_apple += 1

    for orange in oranges:
        if b + orange >= s and b + orange <= t:
            land_orange += 1

    print(land_apple)
    print(land_orange)
