# https://leetcode.com/problems/max-area-of-island/

# bfs on islands
# update biggest islands

import collections
def maxAreaOfIsland(grid) -> int:
    
    max_island = 0
    visited = set()
    num_row, num_col = len(grid), len(grid[0])
    
    def get_neighbors(node):
        delta_r = [-1, 0, 1, 0]
        delta_c = [0, -1, 0, 1]
        
        for i in range(len(delta_r)):
            r, c = node[0] + delta_r[i], node[1] + delta_c[i]
            
            if 0 <= r < num_row and 0 <= c < num_col:
                yield r, c

                
    def bfs(root):
        
        q = collections.deque()
        q.append(root)
        r, c = root
        visited.add((r,c))
        count = 1
        cur_island = 0
        
        while q:
            node = q.popleft()
            for neighbor in get_neighbors(node):
                row, col = neighbor
                if grid[row][col] == 1 and (row,col) not in visited:
                    count += 1
                    visited.add((row,col))
                    q.append((row, col))
            
            cur_island = max(cur_island, count)
        return cur_island
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            if grid[i][j] == 1 and (i,j) not in visited:
                
                island = bfs((i,j))
                
                if island > max_island:
                    max_island = island
                    
    
    return max_island