class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        def traverse(num):
            if num in visited:
                return False
            if num in checked:
                    return True

            lst = preMap[num]
            visited.add(num)

            for nm in preMap[num]:
                if not traverse(nm):
                    return False
            visited.remove(num)
            checked.add(num)
            return True



        for crs in range(numCourses):
            if not traverse(crs):
                return False
        return True
            # return False

                
            
