class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            temp = 0
            grid[x][y] = 0
            
            if x + 1 <= len(grid) - 1 and grid[x + 1][y] == 1: #down
                temp += dfs(x+1,y)
            if x - 1 >= 0 and grid[x - 1][y] == 1: #up
                temp += dfs(x-1,y)
            if y + 1 <= len(grid[0]) - 1 and grid[x][y+1] == 1: #right
                temp += dfs(x,y+1)
            if y - 1 >= 0 and grid[x][y-1] == 1: #left
                temp += dfs(x,y-1)
            
            return temp + 1

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    res = max(res,dfs(x,y))
        return res
