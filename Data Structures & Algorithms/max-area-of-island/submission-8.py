class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        def dfs(x,y):
            temp = 0
            grid[x][y] = 0

            for ro,co in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = x + ro,co + y

                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    temp += dfs(nr,nc)

            return temp + 1
            

        res = 0
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    res = max(res,dfs(x,y))
        return res
