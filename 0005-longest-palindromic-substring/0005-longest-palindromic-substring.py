class Solution(object):
    def longestPalindrome(self, s):
        def extend(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        max_sub = ""
        for i in range(len(s)):
            odd_sub = extend(i, i)
            even_sub = extend(i, i+1)

            if len(odd_sub) > len(max_sub):
                max_sub = odd_sub
            if len(even_sub) > len(max_sub):
                max_sub = even_sub

        return max_sub