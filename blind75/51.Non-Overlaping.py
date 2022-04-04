# https://leetcode.com/problems/non-overlapping-intervals/

# draw a picture
# pick the less between to two end values

def eraseOverlapIntervals(intervals) -> int:
        
    intervals.sort()
    preEnd = intervals[0][1]
    count = 0
    
    for start, end in intervals[1:]:
        
        if start >= preEnd:
            # non overlaping
            preEnd = end
        else:
            count += 1
            preEnd = min(end, preEnd)

    return count

'''

[1, 2]  [1, 3]  [2, 3]  [3, 4]

[1, 2]  [1, 2]  [1, 2]

'''