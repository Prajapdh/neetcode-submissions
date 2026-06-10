class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res=0
        l,r=0,len(people)-1
        print(people)
        while l<=r:
            # If we can fit two people, carry them
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            # Else fill the boat with heavy person to get a lighter person to pair with the lth person
            else:
                r-=1
            res+=1
            print(l,r,res)
        return res

                