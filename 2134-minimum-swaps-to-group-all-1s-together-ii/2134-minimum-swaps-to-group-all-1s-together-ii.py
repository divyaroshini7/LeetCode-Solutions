class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)

        if ones <= 1:
            return 0

        arr = nums + nums

        curr = sum(arr[:ones])
        max_ones = curr

        for i in range(ones, len(arr)):
            curr += arr[i] - arr[i - ones]
            max_ones = max(max_ones, curr)

        return ones - max_ones  