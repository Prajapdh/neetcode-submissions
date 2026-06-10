class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # First create an adj list for each char. We use set to avoid duplicate chars in value
        adjList={c:set() for word in words for c in word}

        # Fill the adj list. traverse two words until you find first non-matching char
        for i in range(1,len(words)):
            w1,w2=words[i-1],words[i]
            minLen=min(len(w1), len(w2))

            # If w1 is substring of w2, it is an invalid case
            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            
            # We only traverse until minLen cause we don't have other char to compare to after it
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        
        # Lets perform post-order dfs on given char
        # We perform post-order traversal because we need to first traverse everything and find a cycle, we add a char to result if no cycle was found
        # if a char appers again in the path, we have cycle and the given order is invalid
        res=[]
        visited={}  #char: False(if visited)/True(visited and added to path)

        def dfs(c):
            # If c is already part of the path, cycle found
            if c in visited:
                return visited[c]
            # Add c to path
            visited[c]=True

            for neighbor in adjList[c]:
                if dfs(neighbor):
                    return True
            # We traversed all nodes from this char, no cylcle was found. Remove it from path and add to result
            visited[c]=False
            res.append(c)
        
        # Perform dfs on each char
        for c in adjList:
            # If True is returned, cycle was found, invalid order
            if dfs(c):
                return ""
        
        # reverse the list cause we added the last char first(postorder)
        res.reverse()
        return "".join(res)


            