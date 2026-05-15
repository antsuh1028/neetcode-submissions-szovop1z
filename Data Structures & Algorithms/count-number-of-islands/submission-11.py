from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL = len(grid),len(grid[0])
        
        res = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    res += 1
                    q = deque([(r,c)])

                    while q:
                        ro,co = q.popleft()
                        for addR,addC in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr,nc = ro + addR, co + addC
                            if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                q.append((nr,nc))

                            


        return res
        
