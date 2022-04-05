# https://leetcode.com/problems/number-of-islands/

# use bfs to mark 1s as visted before increasing number of islands
import collections
def numIslands(grid) -> int:
        
    max_rows, max_cols = len(grid), len(grid[0])
    visited = set()
    islands = 0
    
    
    def bfs(r, c):
        
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))
        
        while q:
            row, col = q.popleft()
            poss_dir = [[1,0], [-1,0], [0,1], [0,-1]]
            
            for dr, dc in poss_dir:
                r, c = row + dr, col + dc
                
                if (r in range(max_rows) and c in range(max_cols) and grid[r][c] == '1' and (r,c) not in visited):
                    visited.add((r,c))
                    q.append((r,c))
    

    for row in range(max_rows):
        for col in range(max_cols):
            if grid[row][col] == "1" and (row,col) not in visited:
                bfs(row, col)
                islands += 1
    
    return islands