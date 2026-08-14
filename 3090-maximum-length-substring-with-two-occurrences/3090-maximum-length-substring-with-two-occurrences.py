from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            counts[s[right]] += 1
            
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            
        return max_len