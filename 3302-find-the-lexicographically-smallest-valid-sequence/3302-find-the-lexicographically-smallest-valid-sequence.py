class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        last = [-1] * (m + 1)
        last[m] = n
        
        ptr = n - 1
        for j in range(m - 1, -1, -1):
            while ptr >= 0 and word1[ptr] != word2[j]:
                ptr -= 1
            if ptr >= 0:
                last[j] = ptr
                ptr -= 1
            else:
                break
                
        ans = []
        changed = False
        i = 0
        
        for j in range(m):
            while i < n:
                if word1[i] == word2[j]:
                    ans.append(i)
                    i += 1
                    break
                elif not changed and last[j + 1] > i:
                    ans.append(i)
                    changed = True
                    i += 1
                    break
                i += 1
            else:
                return []
                
        return ans