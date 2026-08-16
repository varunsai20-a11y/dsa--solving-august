from collections import Counter
from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c = Counter(x % 3 for x in stones)
        
        if c[0] % 2 == 0:
            return c[1] > 0 and c[2] > 0
        
        return abs(c[1] - c[2]) > 2