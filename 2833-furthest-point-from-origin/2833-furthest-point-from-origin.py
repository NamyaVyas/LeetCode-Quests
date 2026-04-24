class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        dist1 = 0  # case: '_' -> 'R'
        dist2 = 0  # case: '_' -> 'L'
        
        for ch in moves:
            # Case 1: treat '_' as 'R'
            if ch == 'R' or ch == '_':
                dist1 += 1
            else:  # 'L'
                dist1 -= 1
            
            # Case 2: treat '_' as 'L'
            if ch == 'L' or ch == '_':
                dist2 -= 1
            else:  # 'R'
                dist2 += 1
        
        return max(abs(dist1), abs(dist2))