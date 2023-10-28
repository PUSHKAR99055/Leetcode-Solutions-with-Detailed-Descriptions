class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        curr = {'b':0, 'a': 0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if i in curr:
                curr[i] += 1
        s = 'balloon'
        return min(curr['b'], curr['a'], curr['n'], curr['l']//2, curr['o']//2)