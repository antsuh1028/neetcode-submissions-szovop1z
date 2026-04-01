class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {num:[] for num in range(numCourses)}
        print(preMap)

        for req in prerequisites:
            preMap[req[0]].append(req[1])
        
        visited = set()
        checked = set()

        def traverse(crs):
            if crs in checked:
                return True
            if not preMap[crs]:
                checked.add(crs)
                return True
            if crs in visited:
                return False
            visited.add(crs)
            
            for num in preMap[crs]:
                if not traverse(num):
                    return False
            checked.add(crs)
            return True

        for n in range(numCourses):
            if not traverse(n):
                return False
        return True
            




