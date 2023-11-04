class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i, target):
            if i == len(coins) or target < 0:
                return float("inf")
            if target == 0:
                return 0
            res = dfs(i+1, target)
            res  = min(res,1 + dfs(i, target - coins[i]))
            return res
        ans = dfs(0, amount)
        return ans if ans != float("inf") else -1