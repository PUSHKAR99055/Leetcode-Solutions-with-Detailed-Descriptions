class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        @cache
        def dfs(i,j):
            res = costs[i][j]
            if i < 0 or i == len(costs) or j < 0 or j == 3:
                return float("inf")
            if i == len(costs)-1 and j >= 0 and j < 3:
                return costs[len(costs)-1][j]
            if j == 1:
                m = min(dfs(i+1,j-1) , dfs(i+1,j+1))
            elif j == 0:
                m = min(dfs(i+1, j+1) , dfs(i+1, j+2))
            elif j == 2:
                m = min(dfs(i+1,j-1) , dfs(i+1,j-2))
            res += m
            return res
        ans = min(dfs(0,0),dfs(0,1),dfs(0,2)) 
        return ans if ans != float("inf") else -1