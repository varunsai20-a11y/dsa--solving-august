from collections import deque
from typing import List


class Solution:

  def lexicographicallySmallestArray(
      self, nums: List[int], limit: int
  ) -> List[int]:
    sorted_nums = sorted(nums)

    num_to_group = {}
    group_to_deque = []

    group_id = 0
    num_to_group[sorted_nums[0]] = group_id
    group_to_deque.append(deque([sorted_nums[0]]))

    for i in range(1, len(sorted_nums)):
      if sorted_nums[i] - sorted_nums[i - 1] > limit:
        group_id += 1
        group_to_deque.append(deque())

      num_to_group[sorted_nums[i]] = group_id
      group_to_deque[group_id].append(sorted_nums[i])

    result = []
    for x in nums:
      gid = num_to_group[x]
      result.append(group_to_deque[gid].popleft())

    return result