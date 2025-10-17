class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        seen = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    triplet = (nums[i], nums[j], nums[k])
                    if triplet not in seen:
                        result.append(list(triplet))
                        seen.add(triplet)
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
        return result