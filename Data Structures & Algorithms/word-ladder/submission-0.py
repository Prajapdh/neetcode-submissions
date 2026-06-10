class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n=len(beginWord)
        nei=collections.defaultdict(list)
        wordList.append(beginWord)
        # create patterns and add all words in that pattern
        for word in wordList:
            for j in range(n):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        print(nei)
        visited=set([beginWord])
        res=1
        queue=deque([beginWord])
        while queue:
            for i in range(len(queue)):
                word=queue.popleft()
                if(word==endWord): return res
                for j in range(n):
                    pattern=word[:j]+"*"+word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            queue.append(neiWord)
            res+=1

        return 0

