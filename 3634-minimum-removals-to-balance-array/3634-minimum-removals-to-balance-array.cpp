class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        
        int n = nums.size();
        int maxKeep = 1;  // At least one element is always valid
        
        int l = 0;
        for (int r = 0; r < n; r++) {
            while ((long long)nums[r] > (long long)nums[l] * k) {
                l++;
            }
            maxKeep = max(maxKeep, r - l + 1);
        }
        
        return n - maxKeep;
    }
};
