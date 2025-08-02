# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen=set()
        seen.add(head.val)
        curr=head
        while curr.next:
            if curr.next.val not in seen:
                seen.add(curr.next.val)
                curr=curr.next
            else:
                curr.next=curr.next.next
            
        return head
        