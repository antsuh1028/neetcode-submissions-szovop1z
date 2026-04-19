class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre = [i for i in nums]
        # post = [i for i in nums]
        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            post[i] = post[i+1] * nums[i+1]

        print(pre,post)
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
            # temp = 1
            # if i < len(nums)-1:
            #     temp *= post[i + 1]
            # if i > 0:
            #     temp *= pre[i-1]
            # res.append(temp)
        return res
            

