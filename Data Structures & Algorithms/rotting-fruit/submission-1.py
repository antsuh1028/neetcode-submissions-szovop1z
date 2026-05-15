from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS = len(grid), len(grid[0])
        q = deque()
        ff_ct = 0
        

        #find all coords of rotten fuits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    ff_ct += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        print(q, ff_ct)

        #bfs 
        time = 0
        while q:
            print(time, q)
            
            times = len(q)
            for _ in range(times):
                ro,co = q.popleft()
                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nr,nc = ro + dr, co + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        ff_ct -= 1
                        q.append((nr,nc))
            if q:
                time += 1

        return time if ff_ct == 0 else -1



