class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    res += 1
                    stack = [(r,c)]

                    while stack:
                        ro,co = stack.pop()
                        if 0 <= ro < ROW and 0 <= co < COL and grid[ro][co] == "1":
                            grid[ro][co] = "0"

                            stack.append((ro+1,co))
                            stack.append((ro-1,co))
                            stack.append((ro,co+1))
                            stack.append((ro,co-1))


        return res
        
