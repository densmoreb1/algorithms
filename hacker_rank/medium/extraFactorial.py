# https://www.hackerrank.com/challenges/extra-long-factorials/problem

def extraLongFactorials(n, new=None):
    if new is None:
        new = 1

    if n <= 1:
        print(new)
    else:
        new *= n
        extraLongFactorials(n - 1, new)


def Fibonacci2(n):
    f = [0] * (n + 2)

    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]
