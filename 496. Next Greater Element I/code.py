class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        l1= [0] * len(nums2)
        curr, ans = {}, []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1][1]:
                index, value = stack.pop()
                curr[nums2[index]] = nums2[i]
            stack.append([i,nums2[i]])
        for i in nums1:
            if i in curr:
                ans.append(curr[i])
            else:
                ans.append(-1)
        return ans
            

