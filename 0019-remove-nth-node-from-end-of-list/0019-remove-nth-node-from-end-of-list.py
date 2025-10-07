# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):        
        cnt = 0
        cur = head                
        while cur:
            cur = cur.next
            cnt += 1
        cnt = cnt - n                      
        dummy = ListNode()             
        dummy.next = head
        cur = dummy
        for _ in range(cnt):
            cur = cur.next
        cur.next = cur.next.next                          
        return dummy.next
        