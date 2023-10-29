class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        curr = collections.defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for i in s:
                alpha[ord(i) - ord('a')] += 1
            curr[tuple(alpha)].append(s)
        values = curr.values()
        return values

        
        