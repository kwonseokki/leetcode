class Solution(object):
    def longestPalindrome(self, s):
        char_cnt = [0] * 52
        res = 0
        odd = 0
        
        for c in s:
            if 'a' <= c <= 'z':
                char_cnt[ord(c)-97] += 1
            elif 'A' <= c <= 'Z':
                char_cnt[ord(c)-65+26] += 1

        for n in char_cnt:
            if n % 2 == 1:
                odd = 1
            res += (n//2) * 2
        return res + odd