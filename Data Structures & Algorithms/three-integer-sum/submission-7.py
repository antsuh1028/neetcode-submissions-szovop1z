class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        res = []
        #[-4, -1, -1, 0, 1, 2]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1,n-1

            while l < r:
                if not nums[i] + nums[l] + nums[r]:
                    res.append([nums[i] , nums[l] , nums[r]])
                    # break
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                    
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res


