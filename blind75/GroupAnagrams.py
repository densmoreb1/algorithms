from collections import defaultdict

def groupAnagrams(strs):
        
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        res[tuple(count)].append(s)
    
    return res.values()


def group2(strs):
    hash = {}
    for s in strs:
        entry = ''.join(sorted(s))
        if entry in hash:
            hash[entry].append(s)
        else:
            hash[entry] = s
        
    return list(hash.values())