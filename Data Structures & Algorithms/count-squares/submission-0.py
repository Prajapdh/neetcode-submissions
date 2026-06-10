class CountSquares:

    def __init__(self):
        self.ptsMap = defaultdict(int)


    def add(self, point: List[int]) -> None:
        self.ptsMap[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        # Check if you have any points lying on the diagonal
        # if x-y == px-py then it is on the forward slash diagonal
        # if y-x == py-px then it is on the backward slash diagonal
        # If found, check if they aren't equal to query point
        # then check if there are (px, y) and (x, py) points, if yes then increase the count
        x,y = point[0], point[1]
        res=0
        for p in self.ptsMap.keys():
            px,py = p
            if abs(px-x)==abs(py-y) and px!=x and py!=y and ((px,y) in self.ptsMap) and ((x, py) in self.ptsMap):
                res+=self.ptsMap[(px,y)]*self.ptsMap[(x, py)]*self.ptsMap[p]
        return res
                