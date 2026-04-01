class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        res = []

        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            
            if interval[0] <= res[-1][1]:
                end = max(res[-1][1], interval[1])
                res[-1] = [res[-1][0],end]
            else:
                res.append(interval)
        return res

