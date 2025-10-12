class Solution(object):
    def isValid(self, s):
        stack = []
        close_pair = {")":"(", "}":"{", "]":"["}
        for c in s:
            if not stack:
                stack.append(c)
            elif c in close_pair and close_pair[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0