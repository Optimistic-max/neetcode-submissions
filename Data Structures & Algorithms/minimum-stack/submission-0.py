class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_arr or val <= self.min_arr[-1]:
            self.min_arr.append(val)
        
    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.min_arr[-1]:
            self.min_arr.pop()
        
    def top(self) -> int:
        return self.arr[-1]
        
    def getMin(self) -> int:
        return self.min_arr[-1]
