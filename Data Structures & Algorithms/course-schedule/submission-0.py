class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency List
        preMap = {i:[] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)
        
        visited=set()
        def dfs(course):
            # print(visited)
            # Cycle detected
            if course in visited:
                return False
            # return True if no requirements needed
            if len(preMap[course])==0:
                return True

            # add to visit set
            visited.add(course)

            for pre in preMap[course]:
                # return false if the course is repeated
                if not dfs(pre): return False
            
            # no cycles found so far, we are done visiting this course
            # backtracking
            visited.remove(course)
            preMap[course]=[]
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
