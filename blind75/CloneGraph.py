# https://leetcode.com/problems/clone-graph

# use a dict to keep track of node created
# copy the neighbors into the new clone

def cloneGraph(node):
        
    copy_node = {}
    
    def clone(node):
        
        if not node:
            return
        
        # base case if node is already made
        if node in copy_node:
            return copy_node[node]
        
        # create new nodes
        copy = Node(node.val)
        copy_node[node] = copy
        for n in node.neighbors:
            # this goes through the graph and adds neighbors while creating the node
            copy.neighbors.append(clone(n))
        
        return copy
    
    return clone(node)