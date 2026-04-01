class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        count = 0

        for num in nums:
            if num-1 in st: #not the start
                continue
            else:
                temp = 1
                increase = num + 1
                while increase in st:
                    temp += 1
                    increase += 1
                count = max(count, temp)
        return count
