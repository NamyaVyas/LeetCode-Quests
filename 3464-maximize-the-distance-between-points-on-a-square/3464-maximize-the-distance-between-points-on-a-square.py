from bisect import bisect_left

class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        def linearize(x, y):
            if y == 0:    return x
            if x == side: return side + y
            if y == side: return 2 * side + (side - x)
            return 3 * side + (side - y)  # x == 0
        
        P = 4 * side
        pos = sorted(linearize(x, y) for x, y in points)
        n = len(pos)
        ext = pos + [p + P for p in pos]  # circular duplicate
        
        def feasible(d):
            for i in range(n):
                cur, idx = ext[i], i
                for _ in range(k - 1):
                    nxt = bisect_left(ext, cur + d, idx + 1, i + n)
                    if nxt >= i + n:
                        break
                    cur, idx = ext[nxt], nxt
                else:
                    # All k-1 jumps succeeded; check wrap-around
                    if ext[i] + P - cur >= d:
                        return True
            return False
        
        lo, hi, ans = 1, P // k, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                ans = mid; lo = mid + 1
            else:
                hi = mid - 1
        return ans