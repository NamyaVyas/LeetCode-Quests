class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, pr, pc, ch):
            visited[r][c] = True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == ch:
                    if nr == pr and nc == pc:
                        continue
                    if visited[nr][nc]:
                        return True
                    if dfs(nr, nc, r, c, ch):
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False