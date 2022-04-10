# https://leetcode.com/problems/merge-k-sorted-lists/
# loop through lists and send them into the merge function
# 

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
    if len(lists) == 0 or not lists:
        return None

    while len(lists) > 0:
        merged = []
        for i in range(len(lists)):

            l1 = lists[i]
            if i + 1 < len(lists):
                l2 = lists[i+1]
            else:
                l2 = None

            merged.append(merge(l1, l2))

        lists = merged

    return lists[0]

def merge(l1, l2):
    dummy = ListNode(0)
    tail = dummy
    
    while l1 and l2:
        
        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
            
        tail = tail.next
    
    if l1:
        tail.next = l1
    
    if l2:
        tail.next = l2
    
    return dummy.next