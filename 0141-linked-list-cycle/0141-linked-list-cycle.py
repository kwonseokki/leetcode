# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        s = set([])
        cur = head
        while cur is not None:
            if cur in s:
                return True
            s.add(cur)
            cur = cur.next
        return False
        