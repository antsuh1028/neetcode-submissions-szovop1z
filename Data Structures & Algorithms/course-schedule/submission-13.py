class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #populate prereq map
        pre = {n:[] for n in range(numCourses)}
        for req in prerequisites:
            pre[req[0]].append(req[1])

        print(pre)

        #already visited within the recursion, cycle detection
        visited = set()
        #cleared
        cleared = set()

        #dfs
        def dfs(crs):
            #base case
            if crs in cleared:
                return True

            #cycle detected
            if crs in visited:
                return False
            visited.add(crs)

            if not pre[crs]:
                cleared.add(crs)
                return True

            

            #iterative step
            courses = pre[crs]
            for course in courses:
                if not dfs(course):
                    return False
            
            cleared.add(crs)
            visited.remove(crs)
            return True

        #loop through each course number and dfs

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            

                




