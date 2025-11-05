class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # 왼쪽 또는 오른쪽이 정렬되었는지 확인
            if nums[start] <= nums[mid]:
                # start 부터 mid까지 범위에 target이 존재하면 정상적으로 범위를 좁혀나감
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                # 그게 아니라면 start를 mid +1 해서 오른쪽 배열로 이동한다
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1