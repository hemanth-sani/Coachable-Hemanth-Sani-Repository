from collections import deque

class Solution:        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        minute = 0
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==  2:
                    queue.append((i, j, minute))
                elif grid[i][j] ==  1:
                    fresh_oranges += 1
        
        def bfs(queue, fresh_oranges):
            time = 0
            while queue:
                row, col, time = queue.popleft()
                directions = [(-1,0), (1,0), (0,1), (0,-1)]
                for x, y in directions:
                    new_x, new_y = row + x, col + y
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_oranges -= 1
                        queue.append((new_x, new_y, time + 1))
            return fresh_oranges, time
        
        fresh_oranges, minute  = bfs(queue, fresh_oranges)

        if fresh_oranges:
            return -1 
        else:
            return minute

            
        
        
