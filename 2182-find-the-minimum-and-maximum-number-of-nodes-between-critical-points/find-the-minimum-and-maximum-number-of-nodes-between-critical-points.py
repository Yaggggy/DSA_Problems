# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head.next:
            return [-1, -1]
        first_idx = -1
        pre_idx = -1
        pre = head
        head = head.next
        idx = 0
        min_d = int(1e5 + 1)
        while head.next:
            if (head.val > pre.val and head.val > head.next.val) or (head.val < pre.val and head.val < head.next.val):
                if first_idx == -1:
                    first_idx = idx
                    pre_idx = idx
                else:
                    min_d = min(min_d, idx - pre_idx)
                    pre_idx = idx
            pre = head
            head = head.next
            idx += 1
        if pre_idx != first_idx:
            return [min_d, pre_idx - first_idx]
        else:
            return [-1, -1]