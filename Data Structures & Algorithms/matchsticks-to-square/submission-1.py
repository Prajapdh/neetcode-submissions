class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Time: 4^n
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        length = total_length // 4
        edges=[0]*4
        # get the failing cases first. If we encounter number whose additon would make length more than expected, we return false
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i==len(matchsticks):
                print(edges)
                return edges[0]==edges[1]==edges[2]==edges[3]
            
            for e in range(len(edges)):
                if edges[e]+matchsticks[i]<=length:
                    edges[e]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    edges[e]-=matchsticks[i]
                #if addition is larger, no number added
                if edges[e]==0:
                    break
            return False

        return dfs(0)