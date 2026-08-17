from itertools import accumulate
from typing import List


class Solution:

  def stoneGameV(self, stoneValue: List[int]) -> int:
    n = len(stoneValue)
    if n == 1:
      return 0

    pref = [0] + list(accumulate(stoneValue))
    dp = [[0] * n for _ in range(n)]
    maxL = [[0] * n for _ in range(n)]
    maxR = [[0] * n for _ in range(n)]

    # Base cases for single elements
    for i in range(n):
      val = stoneValue[i]
      maxL[i][i] = val
      maxR[i][i] = val

    # Bottom-up interval DP
    for length in range(2, n + 1):
      mid = 0
      for i in range(n - length + 1):
        j = i + length - 1
        total = pref[j + 1] - pref[i]

        # Monotonically shift mid so pref[mid+1] - pref[i] <= total / 2
        if mid < i:
          mid = i
        while mid < j and (pref[mid + 2] - pref[i]) * 2 <= total:
          mid += 1

        res = 0

        # Case 1: left_sum < right_sum for k in [i, mid]
        left_sum = pref[mid + 1] - pref[i]
        if left_sum * 2 < total:
          res = max(res, maxL[i][mid])
        elif left_sum * 2 == total:
          # Exactly equal split
          res = max(res, maxL[i][mid], maxR[mid + 1][j])
          if mid > i:
            res = max(res, maxL[i][mid - 1])
        else:
          if mid > i:
            res = max(res, maxL[i][mid - 1])

        # Case 2: left_sum > right_sum for k in [mid + 1, j - 1]
        start_right = mid + 1 if left_sum * 2 <= total else mid
        if start_right < j:
          res = max(res, maxR[start_right + 1][j])

        dp[i][j] = res
        maxL[i][j] = max(maxL[i][j - 1], total + res)
        maxR[i][j] = max(maxR[i + 1][j], total + res)

    return dp[0][n - 1]