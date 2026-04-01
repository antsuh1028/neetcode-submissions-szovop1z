class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        freq = {n: [] for n in range(0, numCourses)}
        
        for pre in prerequisites:
            freq[pre[0]].append(pre[1])
        
        visited = set()
        checked = set()
        res = []
        print(freq)

        def traverse(crs):
            if crs in visited:
                return False

            

            if crs in checked:
                return True

            if not freq[crs]:
                checked.add(crs)
                res.append(crs)
                return True
            visited.add(crs)

            for num in freq[crs]:
                if not traverse(num):
                    return False
            res.append(crs)
            checked.add(crs)
            visited.remove(crs)
            return True

        for c in range(0,numCourses):
            if not traverse(c):
                return []
            print(c)
        return res
            


