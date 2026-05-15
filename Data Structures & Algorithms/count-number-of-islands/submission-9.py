class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        def dfs(r,c):
            grid[r][c] = "0"

            
            for addR,addC in [(1,0),(-1,0),(0,1),(0,-1)]:
                #edge case
                newR,newC = r + addR if 0 <= r+addR < ROW else r, c + addC if 0 <= c+addC < COL else c
                if grid[newR][newC] == "1":
                    dfs(newR,newC)
            return
        
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
        
