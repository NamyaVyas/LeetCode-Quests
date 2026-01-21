class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        
        for (int p : nums) {
            int trailingOnes = 0;
            int temp = p;
            
            // Count trailing 1s in binary representation of p
            while ((temp & 1) == 1) {
                trailingOnes++;
                temp >>= 1;
            }
            
            if (trailingOnes == 0) {
                // No valid x exists
                ans.push_back(-1);
            } else {
                int k = trailingOnes - 1;
                ans.push_back(p - (1 << k));
            }
        }
        
        return ans;
    }
};
