class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        
        for (int n : nums) {
            if (n == 2) {
                ans.push_back(-1);
                continue;
            }
            
            int temp = n;
            int trailingOnes = 0;
            
            while (temp & 1) {
                trailingOnes++;
                temp >>= 1;
            }
            
            int x = n - (1 << (trailingOnes - 1));
            ans.push_back(x);
        }
        
        return ans;
    }
};