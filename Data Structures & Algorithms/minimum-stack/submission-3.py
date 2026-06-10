class MinStack:

    def __init__(self):
        self.s=[]
        self.mins=[]

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.mins:
            self.mins.append(val)
        # What if you have duplicate min elements
        elif self.mins[-1]>=val:
            self.mins.append(val)

    def pop(self) -> None:
        top=self.s.pop()
        if self.mins[-1]==top:
            self.mins.pop()        

    def top(self) -> int:
        return self.s[-1]        

    def getMin(self) -> int:
        return self.mins[-1]
