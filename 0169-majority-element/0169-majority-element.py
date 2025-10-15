class Solution(object):
    def majorityElement(self, nums):        
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        return max(dict, key=dict.get)         