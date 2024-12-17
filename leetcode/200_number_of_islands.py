class Solution:
    def dfs(self, row, col, grid):
        stack = []
        stack.append((row, col))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while len(stack) > 0:
            position_x, position_y = stack.pop()
            if grid[position_x][position_y] == '1':
                for dx, dy in directions:
                    nx, ny = dx + position_x, dy + position_y
                    if  0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                        stack.append((nx,ny))
                grid[position_x][position_y] = '0'


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island_count += 1
                    self.dfs(i,j,grid)
        return island_count
