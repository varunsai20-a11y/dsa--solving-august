from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            min_opponent_score = float('inf')
            
            for X in range(1, 2 * M + 1):
                next_M = max(M, X)
                opponent_score = dp(i + X, next_M)
                min_opponent_score = min(min_opponent_score, opponent_score)
            memo[(i, M)] = suffix_sum[i] - min_opponent_score
            return memo[(i, M)]
        
        return dp(0, 1)