class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.s = list(s)
        
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.pref_char = [''] * (4 * self.n)
        self.suff_char = [''] * (4 * self.n)
        
        self._build(0, 0, self.n - 1)

    def _merge(self, node: int, l_child: int, r_child: int, l_len: int, r_len: int):
        self.pref_char[node] = self.pref_char[l_child]
        self.pref_len[node] = self.pref_len[l_child]
        self.suff_char[node] = self.suff_char[r_child]
        self.suff_len[node] = self.suff_len[r_child]
        
        self.max_len[node] = max(self.max_len[l_child], self.max_len[r_child])
        
        if self.suff_char[l_child] == self.pref_char[r_child]:
            cross_len = self.suff_len[l_child] + self.pref_len[r_child]
            self.max_len[node] = max(self.max_len[node], cross_len)
            
            if self.pref_len[l_child] == l_len:
                self.pref_len[node] = l_len + self.pref_len[r_child]
            
            if self.suff_len[r_child] == r_len:
                self.suff_len[node] = r_len + self.suff_len[l_child]

    def _build(self, node: int, start: int, end: int):
        if start == end:
            char = self.s[start]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.pref_char[node] = char
            self.suff_char[node] = char
            return
        
        mid = (start + end) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2
        
        self._build(left_child, start, mid)
        self._build(right_child, mid + 1, end)
        
        self._merge(node, left_child, right_child, mid - start + 1, end - mid)

    def update(self, node: int, start: int, end: int, idx: int, ch: str):
        if start == end:
            self.s[idx] = ch
            self.pref_char[node] = ch
            self.suff_char[node] = ch
            return
            
        mid = (start + end) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2
        
        if idx <= mid:
            self.update(left_child, start, mid, idx, ch)
        else:
            self.update(right_child, mid + 1, end, idx, ch)
            
        self._merge(node, left_child, right_child, mid - start + 1, end - mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        tree = SegmentTree(s)
        ans = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(0, 0, len(s) - 1, idx, ch)
            ans.append(tree.max_len[0])
            
        return ans