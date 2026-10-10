from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(
        self, heights: List[List[int]]
    ) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            visited = {(r, c)}
            pacific = False
            atlantic = False

            while queue:
                i, j = queue.popleft()

                # This reachable cell already drains to both oceans.
                if (i, j) in res:
                    return True

                if i == 0 or j == 0:
                    pacific = True

                if i == ROWS - 1 or j == COLS - 1:
                    atlantic = True

                if pacific and atlantic:
                    return True

                for dx, dy in directions:
                    x, y = i + dx, j + dy

                    if (
                        0 <= x < ROWS
                        and 0 <= y < COLS
                        and (x, y) not in visited
                        and heights[x][y] <= heights[i][j]
                    ):
                        visited.add((x, y))
                        queue.append((x, y))

            return False

        for i in range(ROWS):
            for j in range(COLS):
                if bfs(i, j):
                    res.add((i, j))

        return [[r, c] for r, c in res]