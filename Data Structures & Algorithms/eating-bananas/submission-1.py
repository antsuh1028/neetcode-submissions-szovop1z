class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc(num):
            summ = 0
            for pile in piles:
                times = pile // num
                print("time",times)
                remain = 1 if pile % num != 0 else 0
                print("remain",remain)
                summ += times + remain
                if summ > h:
                    return False
            print(summ, h, summ <= h)
            return summ <= h


        #nums = [num for num in range(1,max(piles)+1)]
        #print(nums)
        l,r = 1, max(piles)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            
            num = mid

            
            if calc(num):
                res = num
                r = mid - 1
            else:
                l = mid + 1
        return res
            
        print(calc(2))