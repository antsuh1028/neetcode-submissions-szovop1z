class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #o(n) space solution
        has = {}

        for num in nums:
            has[num] = has.get(num, 0) + 1
            if has[num] >= 2:
                return num
        return -1