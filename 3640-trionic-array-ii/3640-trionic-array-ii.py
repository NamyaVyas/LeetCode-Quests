from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        NEG_INF = -10**15   # safely inside 2^53
        
        dp0 = [NEG_INF] * n  # start
        dp1 = [NEG_INF] * n  # inc
        dp2 = [NEG_INF] * n  # inc -> dec
        dp3 = [NEG_INF] * n  # inc -> dec -> inc
        
        dp0[0] = nums[0]
        
        for i in range(1, n):
            # You can ALWAYS start fresh at i
            dp0[i] = nums[i]
            
            if nums[i] > nums[i - 1]:
                dp1[i] = max(
                    dp1[i - 1] + nums[i],
                    dp0[i - 1] + nums[i]
                )
                dp3[i] = max(
                    dp3[i - 1] + nums[i],
                    dp2[i - 1] + nums[i]
                )
            
            elif nums[i] < nums[i - 1]:
                dp2[i] = max(
                    dp2[i - 1] + nums[i],
                    dp1[i - 1] + nums[i]
                )
        
        return max(dp3)
