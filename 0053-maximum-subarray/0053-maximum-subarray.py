class Solution:
    def maxSubArray(self, nums: List[int]) -> iny:
        ans = s = nums[0]

        for i in nums[1:]:
            s = max(i, s + i)
            ans = max(ans, s)

        return ans 