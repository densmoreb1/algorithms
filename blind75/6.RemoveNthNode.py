# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# use a dummy node to offset where the pointer is and use two pointers

def removeNthFromEnd(head, n: int):
        
    # two pointers
    
    # use a dummy node to offset the left pointer
    dummy = ListNode(0, head)
    left = dummy
    right = head
    
    # create the right pointer with a loop
    while n > 0 and right is not None:
        right = right.next
        n -= 1
    
    # with everything offset 
    # we can find the end of the list and the left will be where it's supposed to
    while right:
        left = left.next
        right = right.next
    
    left.next = left.next.next
    
    return dummy.next