class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [i for i in nums]
        post = [i for i in nums]

        temp = 1
        for i in range(len(nums)):
            pre[i] *= temp
            temp  = pre[i]
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] *= temp
            temp  = post[i]
        print(pre,post)

        for i in range(len(nums)):
            res = 1
            if i-1 > -1:
                res *= pre[i-1]
            if i+1 < len(nums):
                res *= post[i+1]
            nums[i] = res
        return nums