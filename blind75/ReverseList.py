def reverseList(head):
        
    if head == None or head.next == None:
        return head
    
    to_do = head.next
    
    reverse = head
    reverse.next = None
    
    while to_do != None:
        temp = to_do
        to_do = to_do.next
        
        temp.next = reverse
        reverse = temp
    return reverse