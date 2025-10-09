class Solution(object):
    def merge(self, nums1, m, nums2, n):
        num1_index = 0
        num2_index = 0
        arr = []
        while num1_index < m and num2_index < n:
            if nums1[num1_index] <= nums2[num2_index]:
                arr.append(nums1[num1_index])
                num1_index += 1
            else:
                arr.append(nums2[num2_index])
                num2_index += 1
        while num1_index < m:
            arr.append(nums1[num1_index])
            num1_index += 1
        while num2_index < n:
            arr.append(nums2[num2_index])
            num2_index += 1
        nums1[:] = arr
        