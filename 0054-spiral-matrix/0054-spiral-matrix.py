class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []

        # 방문하지 않은 부분의 경계값
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 상단 탐색 left부터 right까지
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # 우변 탐색 아래로 진행
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # 아래쪽 행이 남아있는 경우에만 추가
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # 왼쪽열이 남아있을때만 추가
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result