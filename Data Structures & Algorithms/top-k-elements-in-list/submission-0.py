class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for num in nums:
            dct[num] = 1 + dct.get(num,0)
        
        lst = []
        for nm, ct in dct.items():
            lst.append([ct, nm])
        lst.sort()

        final = []
        while len(final) < k:
            final.append(lst.pop()[1])
        return final