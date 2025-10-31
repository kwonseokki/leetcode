class Solution(object):
    def findAnagrams(self, s, p):
        len_s = len(s)
        len_p = len(p)
        p_dict = {}
        s_dict = {}
        answer = []

        for c in p:
            if c in p_dict:
                p_dict[c] += 1
            else:
                p_dict[c] = 1

        for c in s[0:len_p]:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        if p_dict == s_dict:
            answer.append(0)

        for i in range(1, len_s - len_p + 1):
            del_ch = s[i - 1]
            add_ch = s[i + len_p - 1]

            if del_ch in s_dict:
                if s_dict[del_ch] == 1:
                    del s_dict[del_ch]
                else:
                    s_dict[del_ch] -= 1

            if add_ch in s_dict:
                s_dict[add_ch] += 1
            else:
                s_dict[add_ch] = 1
            if p_dict == s_dict:
                answer.append(i)
                
        return answer