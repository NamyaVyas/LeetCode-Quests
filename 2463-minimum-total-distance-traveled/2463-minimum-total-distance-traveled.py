class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        n = len(robot)
        INF = float('inf')
        dp = [0] + [INF] * n  # dp[i] = min cost to assign first i robots

        for pos, limit in factory:
            # Traverse in reverse so each factory is used at most `limit` times
            for i in range(n, 0, -1):
                cost = 0
                for k in range(1, min(i, limit) + 1):
                    cost += abs(robot[i - k] - pos)
                    if dp[i - k] < INF:
                        dp[i] = min(dp[i], dp[i - k] + cost)

        return dp[n]