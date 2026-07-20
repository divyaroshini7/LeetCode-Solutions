class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            x = abs(nums[i]) - 1
            if nums[x] < 0:
                res.append(x + 1)
            else:
                nums[x] = -nums[x]
        return res