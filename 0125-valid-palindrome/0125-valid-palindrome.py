class Solution(object):
    def isPalindrome(self, s):
        s = [c.lower() for c in s if 97 <= ord(c.lower()) <= 122 or 47 <= ord(c) <= 57]
        while len(s) > 1:
            if s.pop() != s.pop(0):
                return False
        return True