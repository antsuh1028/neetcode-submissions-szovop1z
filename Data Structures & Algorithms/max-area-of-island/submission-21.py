class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # helper func dfs to all other land neighbors, every recursion, increment area by 1
        #in double for loop, take max of area and then return

        ROWS, COLS = len(grid), len(grid[0])
        incr = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()

        def isLand(r,c):
            visited.add((r,c))
            area = 1
            grid[r][c] = 0
            for dr,dc in incr:
                nr,nc = r + dr, c + dc
                if (nr, nc) not in visited and 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    area += isLand(nr,nc)

            return area
            
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                temp_area = 0
                if grid[row][col] == 1 and (row,col) not in visited:
                    temp_area = isLand(row,col)
                max_area = max(max_area, temp_area)

        return max_area
