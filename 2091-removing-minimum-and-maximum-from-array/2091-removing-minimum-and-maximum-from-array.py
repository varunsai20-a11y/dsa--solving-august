class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        low = min(min_idx, max_idx)
        high = max(min_idx, max_idx)

        front_only = high + 1

        back_only = n - low

        both_ends = (low + 1) + (n - high)

        return min(front_only, back_only, both_ends)