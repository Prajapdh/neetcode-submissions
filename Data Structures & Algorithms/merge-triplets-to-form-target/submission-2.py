class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        possible=set()  # used to store the index of the matching element

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            # if any value from this triplet matches any value of target
            for i, v in enumerate(t):
                if v==target[i]:
                    possible.add(i)
        
        # if we were able to find matching values for all indices
        return len(possible)==3