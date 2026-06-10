class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False

        # add the count of all elements in the Hashmap
        count={}
        for card in hand:
            count[card]=1+count.get(card, 0)
        
        # We will use the minHeap to find the minimum value from the remaining values
        minHeap=list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first=minHeap[0]
            # print("first: ", first)
            for i in range(first, first+groupSize):
                # print(count)
                # if the consecutive element doesn't exist
                if i not in count:
                    return False
                count[i]-=1
                # remove the value from minHeap if count=0
                if count[i]==0:
                    # when we get out of some value in between(not the minimum value), this breaks the cycle as we still have smaller elements present
                    # without this element, we can't create a group
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True
