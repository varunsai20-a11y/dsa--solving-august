from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n, m = len(s), len(s) // 2
        cnt = Counter(s)
        odds = [c for c, v in cnt.items() if v % 2]
        
        if len(odds) > (n % 2):
            return ""
        
        mid = odds[0] if odds else ""
        pool = {c: cnt[c] // 2 for c in cnt}
        
        def make_pal(pref):
            return pref + mid + pref[::-1] if n % 2 else pref + pref[::-1]

        t_half = target[:m]
        t_cnt = Counter(t_half)
        if all(pool.get(c, 0) >= t_cnt[c] for c in t_cnt):
            cand = make_pal(t_half)
            if cand > target:
                return cand

        cur = Counter(t_half)
        for i in range(m - 1, -1, -1):
            cur[target[i]] -= 1
            if any(cur[c] > pool.get(c, 0) for c in cur):
                continue
            
            rem = {c: pool[c] - cur.get(c, 0) for c in pool}
            valid_c = sorted(c for c in rem if c > target[i] and rem[c] > 0)
            
            if valid_c:
                c = valid_c[0]
                rem[c] -= 1
                tail = "".join(ch * rem[ch] for ch in sorted(rem) if rem[ch] > 0)
                return make_pal(target[:i] + c + tail)

        return ""