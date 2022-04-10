# https://leetcode.com/problems/insert-interval/


# same as merge intervals except add the new interval to the list

def insert(intervals, newInterval):
        
    intervals.append(newInterval)
    intervals.sort()
    
    result = [intervals[0]]
    
    for start, end in intervals:
        lastend = result[-1][1]
        
        if start <= lastend:
            result[-1][1] = max(end, lastend)
        else:
            result.append([start, end])
    
    return result