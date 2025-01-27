"""
When to use BFS over DFS:
    Find nodes close to the root

Data structure:
    Queue pop and popleft

Basic algorithm:
    def bfs_by_queue(root):
        queue = deque([root]) # at least one element in the queue to kick start bfs
        while len(queue) > 0: # as long as there is an element in the queue
            node = queue.popleft() # dequeue
            for child in node.children: # enqueue children
                if OK(child): # early return if problem condition met
                    return FOUND(child)
                queue.append(child)
        return NOT_FOUND
"""
