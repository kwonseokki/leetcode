class Solution(object):
    def search(self, nums, target):
        mid = len(nums) // 2
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return -1
        
        