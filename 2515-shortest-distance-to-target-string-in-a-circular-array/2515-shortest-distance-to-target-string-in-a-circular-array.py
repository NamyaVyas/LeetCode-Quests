class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = float('inf')
        
        for i, word in enumerate(words):
            if word == target:
                dist = abs(i - startIndex)
                min_dist = min(min_dist, dist, n - dist)
        
        return -1 if min_dist == float('inf') else min_dist