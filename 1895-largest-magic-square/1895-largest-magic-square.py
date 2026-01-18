class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Prefix sums
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def isMagic(r, c, k):
            target = row[r][c + k] - row[r][c]

            # check rows
            for i in range(r, r + k):
                if row[i][c + k] - row[i][c] != target:
                    return False

            # check columns
            for j in range(c, c + k):
                if col[r + k][j] - col[r][j] != target:
                    return False

            # check diagonals
            if diag1[r + k][c + k] - diag1[r][c] != target:
                return False
            if diag2[r + k][c] - diag2[r][c + k] != target:
                return False

            return True

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if isMagic(i, j, k):
                        return k

        return 1