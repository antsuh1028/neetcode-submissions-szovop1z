class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(x,y):
            #base case
            if grid[x][y] == "0":
                return

            if grid[x][y] == "1":
                grid[x][y] = "X"
            
            #go through neighbors
            if y + 1 < len(grid[0]) and grid[x][y+1] == "1":
                dfs(x,y+1)
            if x - 1 >= 0 and grid[x-1][y] == "1":
                dfs(x-1,y)
            if y - 1 >= 0 and grid[x][y-1] == "1":
                dfs(x,y-1)
            if x + 1 < len(grid) and grid[x+1][y] == "1":
                dfs(x+1,y)
            return

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                print(x,y)
                if grid[x][y] == "1":
                    count += 1
                    dfs(x,y)
        return count






            