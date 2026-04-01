class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for i in range(len(nums)+1)]
        dct = {}
        res = []

        for num in nums:
            dct[num] = dct.get(num,0) + 1
        print(dct)

        for num in dct:
            print(num)
            arr[dct[num]].append(num)
        print(arr)

        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)
                if len(res) == k:
                    return res




        

        