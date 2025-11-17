class Solution(object):
    def floodFill(self, image, sr, sc, color):
        n = len(image)
        m = len(image[0])
        sp = image[sr][sc]

        if color == sp:
            return image

        def fill(sr, sc):
            if sr < 0 or sr >= n or sc < 0 or sc >= m:
                return

            if image[sr][sc] == sp:
                image[sr][sc] = color
            else:
                return

            fill(sr+1, sc)
            fill(sr-1, sc)
            fill(sr, sc+1)
            fill(sr, sc-1)

        fill(sr, sc)
        return image