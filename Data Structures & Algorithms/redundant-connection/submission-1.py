class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find algo
        N=len(edges)    #since there is one cycle, no. of V = no. of E
        parent=[i for i in range(N+1)]  #nodes start from 1
        rank=[1]*(N+1)

        # returns the node's parent
        def find(n):
            # base case, root node found
            # print(n, parent[n])
            if n==parent[n]:
                return n
            # find the node's root parent
            parent[n]=find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            # cycle detected, both have same root parent
            p1, p2 = find(n1), find(n2)
            if(p1==p2):
                return False
            
            # if a node's parent has a higher rank, attack the lower node to the parent with higher rank
            if(rank[p2]>rank[p1]):
                parent[p1]=p2
                rank[p2]+=rank[p1]
            else:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            return True
        
        for n1,n2 in edges:
            if not union(n1, n2):
                return [n1,n2]
        
            
