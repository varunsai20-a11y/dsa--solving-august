from collections import defaultdict
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_count = defaultdict(int)
        n = len(nums)
        
        for i in range(n - k + 1):
            unique_in_window = set(nums[i:i + k])
            for num in unique_in_window:
                subarray_count[num] += 1
                
        candidates = [num for num, count in subarray_count.items() if count == 1]
        
        return max(candidates) if candidates else -1