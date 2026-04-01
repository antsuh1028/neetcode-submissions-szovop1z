class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calc(num):
            summ = 0
            for pile in piles:
               # times = pile // num
                
                #remain = 1 if pile % num != 0 else 0
                summ +=(pile + num -1) // num
               # summ += times + remain
                if summ > h:
                    return False
            
            return summ <= h

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