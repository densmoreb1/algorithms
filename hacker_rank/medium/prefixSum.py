def getPrefixScores(arr):
    # Write your code here
    new = []
    for i in range(len(arr)):
        prefix = arr[:i + 1]
        to_add = max(prefix)
        op_list = list(map(lambda x: x + (to_add), prefix))
        print(prefix, op_list)
        new.append(sum(op_list))
    
    print(new)

getPrefixScores([1,2,1])