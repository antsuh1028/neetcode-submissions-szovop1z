class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #str type 0 or 1
        #go through each point, see if 1, then look at all neighbors and recursively check them for 
        #1 neighbors
        #increment total islands by 1 after recursion

        ROWS,COLS = len(grid), len(grid[0])
        incr = [[0,1],[1,0],[-1,0],[0,-1]]
        # recursion function for dfs
        def isLand(r,c):
            grid[r][c] = "0"

            #neighbor check
            for dr,dc in incr:
                nr,nc = r + dr, c + dc
                #check if in bound and if point == 1
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1":
                    isLand(nr,nc)

            return

        
        # double for loop to check each point
        
        num_islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    num_islands += 1
                    isLand(row,col)

        return num_islands



        

