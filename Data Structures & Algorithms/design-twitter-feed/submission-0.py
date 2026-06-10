class Twitter:
    def __init__(self):
        self.count = 0  # this keeps decreasing, by using minHeap we can get the latest tweet with lowest value(In other languages we can use maxHeap)
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        minHeap=[]  # stores the most recent tweet by all the user's followers
        # the user follows himself
        self.followMap[userId].add(userId)
        # we store all tweets by followers in a list
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                # getting the last count and tweetId
                count, tweetId = self.tweetMap[followeeId][index]
                # we the store the index of second most recent tweet by that user as well
                # we will use it to replace this if it is used/popped
                heapq.heappush(minHeap, [count, tweetId, followeeId,index-1])
        
        while minHeap and len(res)<10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # if the user has more than one tweet
            if (index>=0):
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId,index-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
