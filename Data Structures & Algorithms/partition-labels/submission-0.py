class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            # end is the max of last index of each character
            end = max(end, lastIndex[c])

            # if end=i, then we have been through all characters in this range
            if i == end:
                res.append(size)
                size = 0
        return res