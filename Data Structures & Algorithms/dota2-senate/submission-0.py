class Solution:
    def predictPartyVictory(self, senate: str) -> str:
    # two rights: ban one senetor's right, all remaining senators with rights are from the same party-he declares win
        rQueue, dQueue = collections.deque(), collections.deque()
        n=len(senate)
        for i,s in enumerate(senate):
            if s=="R":
                rQueue.append(i)
            else:
                dQueue.append(i)
        
        while rQueue and dQueue:
            r,d = rQueue.popleft(), dQueue.popleft()
            # if R senate appears before D, it can ban D and join the queue back and vice versa
            if r<d:
                rQueue.append(r+n)
            else:
                dQueue.append(d+n)
        
        return "Radiant" if rQueue else "Dire"