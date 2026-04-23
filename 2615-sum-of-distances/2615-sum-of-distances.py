from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Group indices by value
        groups = defaultdict(list)
        for i, v in enumerate(nums):
            groups[v].append(i)
        
        arr = [0] * len(nums)
        
        for indices in groups.values():
            n = len(indices)
            if n == 1:
                continue  # arr[i] stays 0
            
            # Build prefix sum of indices
            prefix = [0] * (n + 1)
            for k, idx in enumerate(indices):
                prefix[k + 1] = prefix[k] + idx
            
            total = prefix[n]
            
            for k, idx in enumerate(indices):
                # Elements to the left of k (indices 0..k-1)
                left_count = k
                left_sum = prefix[k]
                left_contrib = idx * left_count - left_sum
                
                # Elements to the right of k (indices k+1..n-1)
                right_count = n - k - 1
                right_sum = total - prefix[k + 1]
                right_contrib = right_sum - idx * right_count
                
                arr[idx] = left_contrib + right_contrib
        
        return arr