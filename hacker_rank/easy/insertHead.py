# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
# insert head of a single linked list

def insertNodeAtHead(llist_head, data):
    new_node = SinglyLinkedListNode(data)
    new_node.next = llist_head
    return new_node