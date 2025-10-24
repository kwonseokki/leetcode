class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substr = []
        max_len = 0
        for c in s:
            if c in substr:
                substr = substr[substr.index(c)+1:]
            substr.append(c)
            max_len = max(max_len, len(substr))
        return max_len