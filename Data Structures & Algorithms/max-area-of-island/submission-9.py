class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col = len(grid), len(grid[0])
        # def dfs(x,y):
        #     temp = 0
        #     grid[x][y] = 0

        #     for ro,co in [(1,0),(-1,0),(0,1),(0,-1)]:
        #         nr,nc = x + ro,co + y

        #         if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
        #             temp += dfs(nr,nc)

        #     return temp + 1
            

        res = 0
        stack = []
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    temp = 0
                    stack.append((r,c))

                    while stack:
                        ro,co = stack.pop()
                        if 0 <= ro < row and 0 <= co < col and grid[ro][co] == 1:
                            grid[ro][co] = 0
                            temp += 1
                            stack.append((ro + 1,co))
                            stack.append((ro - 1,co))
                            stack.append((ro,co + 1))
                            stack.append((ro,co - 1))
                    res = max(res, temp)


        return res
