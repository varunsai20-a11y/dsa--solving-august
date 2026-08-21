import math
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        filtered_coins = []
        for c in coins:
            if not any(c % existing == 0 for existing in filtered_coins):
                filtered_coins.append(c)
        coins = filtered_coins
        n = len(coins)

        subsets = []
        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for combo in combinations(coins, r):
                lcm_val = combo[0]
                for x in combo[1:]:
                    lcm_val = math.lcm(lcm_val, x)
                subsets.append((lcm_val, sign))

        def count_le(m: int) -> int:
            return sum(sign * (m // lcm_val) for lcm_val, sign in subsets)


        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_le(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans