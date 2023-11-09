class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for i,j in prerequisites:
            graph[i].append(j)
        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if graph[i] == []:
                return True
            visit.add(i)
            for j in graph[i]:
                if not dfs(j): return False
            visit.remove(i)
            graph[i] = []
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True
