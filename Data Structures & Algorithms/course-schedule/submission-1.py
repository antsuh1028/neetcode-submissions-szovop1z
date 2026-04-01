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
            print(num)
            lst = preMap[num].copy()
            print(lst)
            if not lst:
                checked.add(num)
                return True

            if num in visited:
                print(num)
                if num in checked:
                    return True
                return False
            visited.add(num)
            for i in range(len(preMap[num])):
                nm = preMap[num][i]
                if traverse(nm):
                    lst.remove(nm)
                else:
                    return False
            preMap[num] = lst
            
            checked.add(num)
            return True



        for crs in range(numCourses):
            ans = traverse(crs)
            if not ans:
                return False
        return True
            # return False

                
            
