class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #edge cases
        if len(heights) == 0:
            return []


        def dfs(r: int, c: int, visited: set):
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc = r + dr,c + dc
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    visited.add((nr,nc))
                    dfs(nr,nc,visited)
            return

        # atlantic
        visited_atlantic = set()
        last_row = len(heights)-1
        last_col = len(heights[0])-1
        col = len(heights[-1])
        row = len(heights)
        for c in range(col):
            if (last_row,c) in visited_atlantic:
                continue
            visited_atlantic.add((last_row,c))
            dfs(last_row,c,visited_atlantic)
        for r in range(row):
            if (r,last_col) in visited_atlantic:
                continue
            visited_atlantic.add((r,last_col))
            dfs(r,last_col,visited_atlantic)


        #pacific
        visited_pacific = set()
        for c in range(col):
            if (0,c) in visited_pacific:
                continue
            visited_pacific.add((0,c))
            dfs(0,c,visited_pacific)
        for r in range(row):
            if (r,0) in visited_pacific:
                continue
            visited_pacific.add((r,0))
            dfs(r,0,visited_pacific)
        return [[r,c] for r,c in visited_atlantic.intersection(visited_pacific)]



