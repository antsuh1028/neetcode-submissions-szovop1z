class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x,y):
            # if grid[x][y] == "0":
            #     return
            if grid[x][y] == "1":
                grid[x][y] = "X"
            
            if x + 1 <= len(grid) - 1 and grid[x + 1][y] == "1": #down
                dfs(x+1,y)
            if x - 1 >= 0 and grid[x - 1][y] == "1": #up
                dfs(x-1,y)
            if y + 1 <= len(grid[0]) - 1 and grid[x][y+1] == "1": #right
                dfs(x,y+1)
            if y - 1 >= 0 and grid[x][y-1] == "1": #left
                dfs(x,y-1)
            
            return

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1
                    dfs(x,y)
        return res
