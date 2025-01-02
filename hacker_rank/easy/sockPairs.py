# https://www.hackerrank.com/challenges/sock-merchant/problem
# finds pairs from an array

def sockMerchant(n, ar):
    pairs = dict()

    for sock in ar:
        if sock not in pairs:
            pairs[sock] = 1
        else:
            pairs[sock] += 1

    pair_count = 0
    # {10: 4, 20: 3, 30: 1, 50: 1}
    pair_count = sum(value // 2 for value in pairs.values())

    print(pairs, pair_count)
    return pair_count
