class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(r,c):
            grid[r][c] = "0"

            
            for addR,addC in [(1,0),(-1,0),(0,1),(0,-1)]:
                #edge case
                print("-",r,c)
                newR,newC = r + addR if 0 <= r+addR < len(grid) else r, c + addC if 0 <= c+addC < len(grid[0]) else c
                print(newR,newC)
                if grid[newR][newC] == "1":
                    dfs(newR,newC)
            return
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        print(grid)
        return res
        
