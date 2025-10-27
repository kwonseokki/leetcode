class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign = 1
        num_str = ""

        i = 0
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            i += 1
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1

        if not num_str:
            return 0

        res = sign * int(num_str)
        max_32bit = 2**31 - 1
        min_32bit = -2**31
        res = max(min(res, max_32bit), min_32bit)
        return res