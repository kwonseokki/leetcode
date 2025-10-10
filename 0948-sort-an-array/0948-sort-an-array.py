class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        return self.merge(self.sortArray(left_arr), self.sortArray(right_arr))
        
    def merge(self, arr1, arr2):
        result = []
        arr1_index = 0
        arr2_index = 0
        while arr1_index < len(arr1) and arr2_index < len(arr2):
            if arr1[arr1_index] <= arr2[arr2_index]:
                result.append(arr1[arr1_index])
                arr1_index += 1
            else:
                result.append(arr2[arr2_index])
                arr2_index += 1
        while arr1_index < len(arr1):
            result.append(arr1[arr1_index])
            arr1_index += 1
        while arr2_index < len(arr2):
            result.append(arr2[arr2_index])
            arr2_index += 1
        return result    
