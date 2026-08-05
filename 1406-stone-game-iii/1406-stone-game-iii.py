class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            current_sum = 0
            
            for k in range(1, 4):
                if i + k <= n:
                    current_sum += stoneValue[i + k - 1]
                    dp[i] = max(dp[i], current_sum - dp[i + k])
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

        