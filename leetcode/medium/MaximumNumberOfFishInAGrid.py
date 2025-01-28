# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

# land cell grid[r][c] = 0
# water/fish cell grid[r][c] > 1
def find_max_fish(grid):

    num_rows = len(grid)
    num_cols = len(grid[0])

    def get_neighbors(coords):
        res = []
        row, col = coords
        d_row = [-1, 0, 1, 0]
        d_col = [0, -1, 0, 1]

        for i in range(len(d_row)):
            r = row + d_row[i]
            c = col + d_col[i]
            if 0 <= r < num_rows and 0 <= c < num_cols:
                res.append((r, c))

        return res

    def bfs(r, c):
        queue = [(r, c)]
        cur = 0
        visted = set()

        while len(queue) > 0:
            row, col = queue.pop(0)
            if (row, col) not in visted:
                visted.add((row, col))
                cur += grid[row][col]
            print(row, col, 'adding', grid[row][col], 'visited', visted)

            for r, c in get_neighbors((row, col)):
                cell = grid[r][c]
                print(r, c)
                if cell > 0 and (r, c) not in visted:
                    queue.append((r, c))

            print(cur)

        return cur

    mega_max = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            print(r, c)
            if grid[r][c] > 0:
                print('Starting at:', (r, c))
                mega_max = max(bfs(r, c), mega_max)

    return mega_max


# grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
# grid = [[0, 4]]
grid = [[8, 6], [2, 6]]
print(find_max_fish(grid))
