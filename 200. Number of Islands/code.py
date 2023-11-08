class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            visit.add((r,c))
            for dr, dc in directions:
                row, col = r+dr, c+dc
                if row in range(ROWS) and col in range(COLS) and (row,col) not in visit and grid[r][c] == '1':
                    dfs(row, col)
            return 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in visit:
                    dfs(r,c)
                    res += 1
        return res
