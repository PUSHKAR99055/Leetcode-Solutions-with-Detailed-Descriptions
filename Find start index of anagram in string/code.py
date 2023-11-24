class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        curr, purr = {}, {}
        if len(s) < len(p):
            return []
        for i in range(len(p)):
            curr[s[i]] = 1 + curr.get(s[i], 0)
            purr[p[i]] = 1 + purr.get(p[i], 0)
        res = [0] if curr == purr else []
        l, r = 0, len(p)
        while r < len(s):
            curr[s[r]] = 1 + curr.get(s[r], 0)
            curr[s[l]] -= 1
            if curr[s[l]] == 0:
                curr.pop(s[l])
            l += 1
            if curr == purr:
                res.append(l)
            r += 1
        return res

        