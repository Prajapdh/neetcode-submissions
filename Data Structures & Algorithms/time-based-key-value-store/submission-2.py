class TimeMap:

    def __init__(self):
        self.mapp=collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f"K: {key}, v: {value}, t: {timestamp}")
        self.mapp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        print(f"get: k={key}, t={timestamp}")
        values=self.mapp[key]
        print(values)
        if not values:
            return ""
        res=""
        l,r=0, len(values)-1
        while(l<=r):
            m=(l+r)//2
            if(values[m][0]<=timestamp):
                res=values[m][1]
                l=m+1
            else:
                r=m-1
        return res
