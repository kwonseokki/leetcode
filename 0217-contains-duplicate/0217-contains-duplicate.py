class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        for val in dict.values():
            if val > 1:
                return True
        return False
        