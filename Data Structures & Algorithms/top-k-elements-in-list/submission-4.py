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

        i = len(arr)-1
        while len(res) < k:
            if arr[i]:
                res.append(arr[i].pop())
            else:
                i-=1 
        return res




        

        