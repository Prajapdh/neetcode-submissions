class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.forwardHistory=[]

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forwardHistory=[]

    def back(self, steps: int) -> str:
        for i in range(min(len(self.history)-1, steps)):
            self.forwardHistory.append(self.history.pop())
        return self.history[-1]

    def forward(self, steps: int) -> str:
        for i in range(min(len(self.forwardHistory), steps)):
            self.history.append(self.forwardHistory.pop())
        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)