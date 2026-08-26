class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        if len(ones) < k:
            return ""
        
        candidates = [
            s[ones[i] : ones[i + k - 1] + 1]
            for i in range(len(ones) - k + 1)
        ]
        
        min_len = min(len(sub) for sub in candidates)
        
        return min(sub for sub in candidates if len(sub) == min_len)