class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for index,num in enumerate(nums):
            new = target - num
            print(new)
            if new in dct:
                return [dct[new], index]

            dct[num] = index
            print(dct)


            