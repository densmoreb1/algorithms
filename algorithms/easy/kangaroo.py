# https://www.hackerrank.com/challenges/kangaroo/problem
# find if two kangaroos meet on the same spot
# given both there jump distance and starting position

def kangaroo(x1, v1, x2, v2):
    # for i in range(1, 100):
    #     if (v1 * i + x1) % (v2 * i + x2) == 0:
    #         return 'YES'
    if (v1 > v2) and (x2 - x1) % (v2 - v1) == 0:
        return "YES"
    else:
        return "NO"