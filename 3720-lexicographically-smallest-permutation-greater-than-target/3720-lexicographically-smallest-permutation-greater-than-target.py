class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        from collections import Counter
        
        counts = Counter(s)
        n = len(s)
        
        matched = 0
        for ch in target:
            if counts[ch] > 0:
                counts[ch] -= 1
                matched += 1
            else:
                break
        
        if matched == n:
            matched -= 1
            counts[target[matched]] += 1
            
        for i in range(matched, -1, -1):
            target_char = target[i]
            
            chosen_char = None
            for code in range(ord(target_char) + 1, ord('z') + 1):
                c = chr(code)
                if counts[c] > 0:
                    chosen_char = c
                    break
            
            if chosen_char is not None:
                counts[chosen_char] -= 1
                suffix = []
                for code in range(ord('a'), ord('z') + 1):
                    c = chr(code)
                    if counts[c] > 0:
                        suffix.append(c * counts[c])
                return target[:i] + chosen_char + "".join(suffix)
            
            if i > 0:
                counts[target[i - 1]] += 1
                
        return ""