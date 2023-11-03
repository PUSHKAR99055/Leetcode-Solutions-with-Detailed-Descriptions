class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hash = set()
        for i in range(0,len(s)-k+1):
            if s[i:i+k] not in hash:
                hash.add(s[i:i+k])
        return len(hash) == pow(2,k)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l , r= 0 , len(matrix)-1
        while l < r:
            top, bottom = l , r
            for i in range(r-l):
                top_left = matrix[top][l + i]
                #bottom left
                matrix[top][l + i] = matrix[bottom - i][l]
                #bottm right
                matrix[bottom - i][l] = matrix[bottom][r-i]
                #top right 
                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = top_left

            l += 1
            r -= 1
        