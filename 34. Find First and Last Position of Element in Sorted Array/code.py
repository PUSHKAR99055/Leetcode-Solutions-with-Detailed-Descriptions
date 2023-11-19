class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:   
        stack = []
        new_height = [-1] * len(heights)
        res = []
        for i in range(len(heights)):
            while stack and heights[i] > stack[-1][1]:
                index, value = stack.pop()
                new_height[index] = i
            stack.append([i,heights[i]])
        for i, j in queries:
            if i > j:
                i, j = j, i
            if i == j:
                res.append(i)
            elif heights[j] > heights[i]:
                res.append(j)
            elif new_height[i] == -1 or new_height[j] == -1:
                res.append(-1)
            else:
                curr = j
                while curr < len(heights) and new_height[curr] != -1 and heights[curr] <= heights[i]:
                    curr = new_height[curr]
                if heights[curr] > heights[i]:
                    res.append(curr)
                else:
                    res.append(-1)
        return res

