# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1
        
        first_cp_index = -1
        prev_cp_index = -1
        min_dist = float('inf')
        
        while curr.next:
            is_critical = (
                (curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)
            )
            
            if is_critical:
                if first_cp_index == -1:
                    first_cp_index = index
                else:
                    min_dist = min(min_dist, index - prev_cp_index)
                
                prev_cp_index = index
            
            prev = curr
            curr = curr.next
            index += 1

        if min_dist == float('inf'):
            return [-1, -1]
        
        max_dist = prev_cp_index - first_cp_index
        return [min_dist, max_dist]