# https://leetcode.com/problems/merge-intervals/

# draw a picture
# assign start and end values and compare to the last

def merge(intervals):
    
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]
    print(output)
    
    for start, end in intervals:
        last = output[-1][1]
        
        if start <= last:
            output[-1][1] = max(last, end)
        else:
            output.append([start, end])
    
    print(output)
    return output