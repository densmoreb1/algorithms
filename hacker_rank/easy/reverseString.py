def reverse_string(s):
    new = ''
    for i in range(len(s) - 1, -1, -1):
        new += s[i]
    print(new)


reverse_string('')

print('55231'[-2])
