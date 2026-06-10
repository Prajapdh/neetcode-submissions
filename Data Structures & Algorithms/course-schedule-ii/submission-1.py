class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # adjacency list
        preMap={i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        pendingCourses=set()
        for i in range(numCourses):
            pendingCourses.add(i)
        res=[]
        visited=set()
        def dfs(course):
            print(course)
            print(f"visited: {visited}")
            print(f"pending: {pendingCourses}")
            print(f"res: {res}")
            # Cycle detected
            if course in visited:
                return False
            if len(preMap[course])==0:
                if course in pendingCourses:
                    res.append(course)
                    pendingCourses.remove(course)
                return True

            visited.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            preMap[course]=[]
            if course in pendingCourses:
                res.append(course)
                pendingCourses.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        res=res+list(pendingCourses)
        return res
