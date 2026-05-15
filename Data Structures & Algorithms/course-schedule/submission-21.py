class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #populate prereq map
        pre = {n:[] for n in range(numCourses)}
        for req in prerequisites:
            pre[req[0]].append(req[1])


        #already visited within the recursion, cycle detection
        visited = set()
        #cleared

        #dfs
        def dfs(crs):
            #base case
            if not pre[crs]:
                return True
            #cycle detected
            if crs in visited:
                return False
            visited.add(crs)
            #iterative step
            for course in pre[crs]:
                if not dfs(course):
                    return False
            
            pre[crs] = []
            visited.remove(crs)
            return True

        #loop through each course number and dfs

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            

                




