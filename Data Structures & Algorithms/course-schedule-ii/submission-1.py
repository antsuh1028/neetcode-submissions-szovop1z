class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        visited = set()
        checked =set()
        for i in range(numCourses):
            preMap[i] = []
        for pre in prerequisites:
            crs = pre[0]
            req = pre[1]
            preMap[crs].append(req)
        print(preMap)

        sched = []
        def traverse(crs):
            if crs in checked:
                visited.add(crs)
                return True
            if crs in visited:
                return False
            visited.add(crs)
            
            for c in preMap[crs]:
                if not traverse(c):
                    return False
                visited.remove(c)
                checked.add(c)
            sched.append(crs)
            checked.add(crs)
            return True

        for i in range(0, numCourses):
            if not traverse(i):
                return []
            print("sched:",sched)
        return sched
        




        