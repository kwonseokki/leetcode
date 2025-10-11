class Solution(object):
    def sortColors(self, nums):
        count = [0] * 3
        arr = []
        for num in nums:
            count[num] += 1
        for i in range(len(count)):
            arr += [i] * count[i]
        nums[:] = arr