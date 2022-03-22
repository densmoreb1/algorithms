# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
# insert not at tail
# unable to test here, see problem

def insertNodeAtTail(head, data):
    if head is None:
        return SinglyLinkedListNode(data)
    else:
        curr = head
        while curr is not None:
            if curr.next == None:
                new_node = SinglyLinkedListNode(data)
                curr.next = new_node
                return head
            curr = curr.next