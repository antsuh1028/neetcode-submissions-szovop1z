class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        past = -10000000

        for i in range(len(nums)):
            print("a", nums[i])
            curr = nums[i]
            if past == curr: #already seen
                continue
            #two sum from here
            l,r = i+1, len(nums)-1
            
            while l < r:
                print(l,r)
                total = curr + nums[l] + nums[r]
                if total == 0:
                    res.append([curr, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif total > 0:
                    r-=1
                    # if nums[r+1] == nums[r]:
                    #     r -= 1
                    while l < r and nums[r+1] == nums[r]:
                        r -= 1
                else:
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                    # if nums[l-1] == nums[l]:
                    #     l += 1
            past = curr
        return res



            



