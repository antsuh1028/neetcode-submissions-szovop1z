class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}

        for i in range(len(nums)):
            num = nums[i]
            difference = target - num
            if difference in dct:
                return [dct[difference], i]
            else:
                dct[num] = i

            
            