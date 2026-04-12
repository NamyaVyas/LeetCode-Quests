class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(a, b):
            if a == 26:  # finger not yet placed — free move
                return 0
            r1, c1 = divmod(a, 6)
            r2, c2 = divmod(b, 6)
            return abs(r1 - r2) + abs(c1 - c2)

        n = len(word)
        # dp[other] = min cost when current finger is at word[i-1], other finger is at `other`
        # Initialize: before typing anything, both fingers are free (26)
        INF = float('inf')
        
        # After typing word[0] with one finger (free), other finger is still free
        dp = [INF] * 27
        dp[26] = 0  # other finger hasn't moved yet; cost = 0 (first char is free)

        for i in range(1, n):
            cur  = ord(word[i-1]) - ord('A')
            nxt  = ord(word[i])   - ord('A')
            new_dp = [INF] * 27

            for other in range(27):
                if dp[other] == INF:
                    continue
                cost = dp[other]

                # Option 1: Move the finger currently at `cur` → `nxt`
                # Other finger stays at `other`
                new_dp[other] = min(new_dp[other], cost + dist(cur, nxt))

                # Option 2: Move the `other` finger → `nxt`
                # Current finger stays at `cur` (becomes the new `other`)
                new_dp[cur] = min(new_dp[cur], cost + dist(other, nxt))

            dp = new_dp

        return min(dp)