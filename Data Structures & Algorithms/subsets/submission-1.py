class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #treat as a decision tree, where you add to the subset or don't add to subset
        #recursivep dfs to add tot eh subset and not

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
        return res