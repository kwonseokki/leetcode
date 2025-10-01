# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        cur = None
        while head is not None:
            cur = head.next
            head.next = prev
            prev = head
            head = cur
        return prev
        