class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First we build an adj List, courses are nodes. directed edge from course to pre-req
        adjList={}
        for c,p in prerequisites:
            if c not in adjList:
                adjList[c]=[]
            adjList[c].append(p)

        visited=set()   # It stores all courses required in the path. If we try to append a course that's already present, cycle found
        
        def dfs(c):
            if c not in adjList:
                return True
            print(c, adjList[c], visited)
            if c in visited:
                return False
            visited.add(c)
            res=True
            for pre in adjList[c]:
                res= res and dfs(pre)
            visited.remove(c)
            return res

        for course in adjList.keys():
            visited=set()
            if not dfs(course):
                return False
        
        return True