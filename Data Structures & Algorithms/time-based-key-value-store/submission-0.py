class TimeMap:

    def __init__(self):
        self.dct = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dct: 
            self.dct[key] = [[value, timestamp]]
        else:
            self.dct[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dct:
            return ""
        
        # if self.dict[key][-1]
        lst = self.dct[key]
        low,high = 0,len(lst)-1
        res = ""

        while low <= high:
            mid =( high+low) // 2

            if lst[mid][1] == timestamp:
                return lst[mid][0]
            elif lst[mid][1] > timestamp:
                high = mid - 1
            else:
                res = lst[mid][0]
                low = mid + 1
        return res


        


        
