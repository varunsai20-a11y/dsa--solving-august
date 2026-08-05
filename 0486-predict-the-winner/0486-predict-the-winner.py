class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def maxDiff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]
            pick_left = nums[i] - maxDiff(i + 1, j)
            pick_right = nums[j] - maxDiff(i, j - 1)

            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        return maxDiff(0, len(nums) - 1) >= 0

        