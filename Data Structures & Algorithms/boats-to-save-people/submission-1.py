class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # each boat can carry up to limit weights and up to 2 people
        # output: min no of boats
        # brute force?
        people.sort()
        l,r = 0, len(people)-1
        res=0
        while l<=r:
            if l!=r and people[l]+people[r]>limit:
                r-=1
            else:
                r-=1
                l+=1
            res+=1
        return res