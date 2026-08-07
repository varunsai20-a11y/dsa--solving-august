class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"

        def get_min_digits(c2, c3, c5, c7):
            digits = [7] * c7 + [5] * c5
            
            n8, c2 = divmod(c2, 3)
            n9, c3 = divmod(c3, 2)
            
            if c2 == 1 and c3 == 1:
                digits.append(6)
                c2, c3 = 0, 0
            elif c2 == 2 and c3 == 1:
                digits.extend([2, 6])
                c2, c3 = 0, 0
            elif c2 == 2 and c3 == 0:
                digits.append(4)
                c2 = 0
            
            if c2 > 0: 
                digits.extend([2] * c2)
            if c3 > 0: 
                digits.extend([3] * c3)
            digits.extend([8] * n8)
            digits.extend([9] * n9)
            
            return digits

        def build_suffix(c2, c3, c5, c7, length):
            min_digits = get_min_digits(c2, c3, c5, c7)
            if len(min_digits) > length:
                return None
            ones_needed = length - len(min_digits)
            res = [1] * ones_needed + sorted(min_digits)
            return "".join(map(str, res))

        n = len(num)
        
        pref2, pref3, pref5, pref7 = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
        first_zero = -1
        
        for i, ch in enumerate(num):
            if ch == '0':
                first_zero = i
                break
            d = int(ch)
            pref2[i+1] = pref2[i] + (1 if d in (2, 6) else 2 if d == 4 else 3 if d == 8 else 0)
            pref3[i+1] = pref3[i] + (1 if d in (3, 6) else 2 if d == 9 else 0)
            pref5[i+1] = pref5[i] + (1 if d == 5 else 0)
            pref7[i+1] = pref7[i] + (1 if d == 7 else 0)

        def needed(cur2, cur3, cur5, cur7):
            return (max(0, counts[2] - cur2),
                    max(0, counts[3] - cur3),
                    max(0, counts[5] - cur5),
                    max(0, counts[7] - cur7))

        if first_zero == -1:
            req2, req3, req5, req7 = needed(pref2[n], pref3[n], pref5[n], pref7[n])
            if req2 == 0 and req3 == 0 and req5 == 0 and req7 == 0:
                return num

        limit = n if first_zero == -1 else first_zero
        
        for i in range(limit, -1, -1):
            start_d = int(num[i]) + 1 if i < n else 10
            for d in range(start_d, 10):
                d2 = (1 if d in (2, 6) else 2 if d == 4 else 3 if d == 8 else 0)
                d3 = (1 if d in (3, 6) else 2 if d == 9 else 0)
                d5 = (1 if d == 5 else 0)
                d7 = (1 if d == 7 else 0)

                req2, req3, req5, req7 = needed(pref2[i] + d2, pref3[i] + d3, pref5[i] + d5, pref7[i] + d7)
                suffix = build_suffix(req2, req3, req5, req7, n - 1 - i)
                if suffix is not None:
                    return num[:i] + str(d) + suffix

        min_digits = get_min_digits(counts[2], counts[3], counts[5], counts[7])
        target_len = max(n + 1, len(min_digits))
        return build_suffix(counts[2], counts[3], counts[5], counts[7], target_len)