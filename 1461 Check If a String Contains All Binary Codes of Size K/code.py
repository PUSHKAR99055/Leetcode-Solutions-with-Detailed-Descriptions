class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hash = set()
        for i in range(0,len(s)-k+1):
            if s[i:i+k] not in hash:
                hash.add(s[i:i+k])
        return len(hash) == pow(2,k)
