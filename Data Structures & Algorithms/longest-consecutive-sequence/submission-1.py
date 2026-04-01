class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        count = 0
        for num in nums:
            temp = 0
            if num-1 not in st:
                while num in st:
                    num += 1
                    temp += 1
                count = max(temp, count)
        return count



        