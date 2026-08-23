class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        left_str, right_str = num[:mid], num[mid:]
        
        left_sum = sum(int(c) for c in left_str if c != '?')
        right_sum = sum(int(c) for c in right_str if c != '?')
        
        left_q = left_str.count('?')
        right_q = right_str.count('?')
        
        return 2 * (left_sum - right_sum) != 9 * (right_q - left_q)