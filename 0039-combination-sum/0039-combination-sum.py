class Solution(object):
    def combinationSum(self, candidates, target):
        return self.backtracking(1, 0, candidates, target, [], [])

    def backtracking(self, depth, start, arr, target, sum_arr, result):
        # 종료조건
        # sum이 target보다 클때
        if target <= sum(sum_arr) or sum(sum_arr) >= 150:
            if target == sum(sum_arr):
                result.append(sum_arr[:])
            return

        for i in range(start, len(arr)):
            sum_arr.append(arr[i])
            self.backtracking(i+1, i, arr, target, sum_arr, result)
            sum_arr.pop()
        return result