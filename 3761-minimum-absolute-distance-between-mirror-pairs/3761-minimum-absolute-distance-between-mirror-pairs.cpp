class Solution {
public:
    int minMirrorPairDistance(vector<int>& nums) {
        auto rev = [](int x) {
            int r = 0;
            while (x > 0) {
                r = r * 10 + x % 10;
                x /= 10;
            }
            return r;
        };
        
        // map from reversed_value -> last index
        unordered_map<int, int> revMap;
        int minDist = INT_MAX;
        
        for (int i = 0; i < (int)nums.size(); i++) {
            // Check if nums[i] matches the reverse of some earlier element
            // i.e., some j < i had rev(nums[j]) == nums[i]
            if (revMap.count(nums[i])) {
                minDist = min(minDist, i - revMap[nums[i]]);
            }
            // Store rev(nums[i]) so future nums[k] == rev(nums[i]) can match
            revMap[rev(nums[i])] = i;
        }
        
        return minDist == INT_MAX ? -1 : minDist;
    }
};