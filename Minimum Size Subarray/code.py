class Solution:
    def minSizeSubarray(self, target, nums):
        l = 0
	sum = 0
	ans = float("inf")
	for i in range(0, len(nums)):
		sum += nums[i]
		while sum >= target:
			ans = min(ans, l-i+1)
			sum -= nums[l]
			l += 1
	return ans if ans != float("inf") else 0            

