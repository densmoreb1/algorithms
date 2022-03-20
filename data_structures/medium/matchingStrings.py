# https://www.hackerrank.com/challenges/sparse-arrays/problem
# given an array and a list of queries
# return a count list of how many are found

def matchingStrings(strings, queries):
    count = []
    
    for i in queries:
        count.append(strings.count(i))
    return count


strings = ['aba', 'baba', 'aba', 'xzxb']
queries = ['aba', 'xzxb','ab']

print(matchingStrings(strings, queries))