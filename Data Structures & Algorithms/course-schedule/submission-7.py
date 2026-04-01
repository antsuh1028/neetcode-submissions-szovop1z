class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {num: [] for num in range(numCourses)}
        visited = set()
        checked = set()

        
        for pre in prerequisites:
            preMap[pre[0]].append(pre[1])
        print(preMap)

        #helper fn for traversing
        def traverse(num):
            print(num)
            if num in visited:
                return False
            if num in checked:
                return True

            # if not preMap[num]:
            #     checked.add(num)
            #     return True

            

            visited.add(num)

            for crs in preMap[num]:
                if not traverse(crs):
                    return False
                # preMap[num].remove(crs)
                print(preMap)
            visited.remove(num)
                
                

            checked.add(num)
            return True
                


        #for each, traverse
        for course in range(0,numCourses):
            if not traverse(course):
                return False
        return True