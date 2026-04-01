class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(num):
            total = 0            
            for pile in piles:
                carry = 1 if pile % num else 0
                total += pile // num + carry
            return total <= h

        max_nana = max(piles)
        min_rate = max_nana
        l,r = 1,max_nana

        while l <= r:
            mid = (l + r) //2
            print(mid)
            if can(mid):
                min_rate = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_rate
                

            