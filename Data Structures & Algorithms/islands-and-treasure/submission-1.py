from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        visited = set()
        #find all rooms and input into queue first
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        print(queue)
        
        

        while queue:
            r,c = queue.popleft()
            dist = grid[r][c] + 1

            for addR,addC in ((1,0),(-1,0),(0,1),(0,-1)):
                newR,newC = r + addR, c + addC
                print(newR,newC)

                if 0 <= newR < len(grid) and 0 <= newC < len(grid[0]) and (newR,newC) not in visited and grid[newR][newC] != -1:
                    grid[newR][newC] = dist
                    queue.append((newR,newC))
                    print(queue)
                    visited.add((newR,newC))
            




