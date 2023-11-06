class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float("inf")
        while l <= r:
            sum = 0
            mid = l + (r-l)//2
            for p in piles:
                print(math.ceil(p / mid) )
                sum += math.ceil(p / mid) 
            if sum <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans
            

