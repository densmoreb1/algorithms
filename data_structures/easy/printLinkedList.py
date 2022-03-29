# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
# unable to test here see problem

def printLinkedList(node):
    if node is not None:
        print(node.data)
        printLinkedList(node.next)
