# https://leetcode.com/problems/linked-list-cycle
# use two pointers and make one go faster than the other
# if the loop breaks then there is no cycle

def hasCycle(head) -> bool:
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False