from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_rows = defaultdict(int)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                reserved_rows[r] |= (1 << c)
        
        total_families = (n - len(reserved_rows)) * 2
        
        LEFT_MASK = 60
        RIGHT_MASK = 960
        MID_MASK = 240
        
        for mask in reserved_rows.values():
            left_open = (mask & LEFT_MASK) == 0
            right_open = (mask & RIGHT_MASK) == 0
            mid_open = (mask & MID_MASK) == 0
            
            if left_open and right_open:
                total_families += 2
            elif left_open or right_open or mid_open:
                total_families += 1
                
        return total_families