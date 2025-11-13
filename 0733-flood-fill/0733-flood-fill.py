class Solution(object):
    def floodFill(self, image, sr, sc, color):
        n = len(image)
        m = len(image[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        sp = image[sr][sc]

        def fill(sr, sc):
            if sr < 0 or sr >= n or sc < 0 or sc >= m:
                return

            if image[sr][sc] == sp:
                image[sr][sc] = color
            else:
                return
            # 이미 방문한경우 함수 종료
            if visited[sr][sc]:
                return
            visited[sr][sc] = True

            fill(sr+1, sc)
            fill(sr-1, sc)
            fill(sr, sc+1)
            fill(sr, sc-1)

        fill(sr, sc)
        return image