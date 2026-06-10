class StockSpanner:

    def __init__(self):
        # We will add an element to the stack if the top most element is higher than current price
        # If not then we will keep popig the last element until above condition is met
        self.stack=[] #stores a pair: (price, index)
        self.curr=0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0]<=price:
            self.stack.pop()
        self.stack.append((price, self.curr))
        self.curr+=1
        # print(price, self.stack if self.stack else [], self.curr)
        return self.stack[-1][1]-self.stack[-2][1] if len(self.stack)>1 else self.curr


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)