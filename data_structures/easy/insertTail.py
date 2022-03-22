# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# unable to test here, see problem
# works for most 

def insertNodeAtTail(head, data):
    if head == None:
        return SinglyLinkedListNode(data)
    else:
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
        else:
            insertNodeAtTail(head.next, data)
        return head
