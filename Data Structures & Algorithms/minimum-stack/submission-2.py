class MinStack:

    def __init__(self):
        self.array = []
        self.extra = []

    def push(self, val: int) -> None:
        self.array.append(val)
        val = min(self.extra[-1] if self.extra else val, val) 
        self.extra.append(val)
        # self.minimum = min(self.minimum, val)
        

    def pop(self) -> None:
        self.array.pop()
        self.extra.pop()
        # self.extra.pop()


    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.extra[-1]
