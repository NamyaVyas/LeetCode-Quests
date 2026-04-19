class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int i = 0, j = 0;
        int maxDist = 0;
        int n = nums1.size(), m = nums2.size();

        while (i < n && j < m) {
            if (nums2[j] >= nums1[i]) {
                // Valid pair: record distance and push j further
                maxDist = max(maxDist, j - i);
                j++;
            } else {
                // nums2[j] < nums1[i]: need a smaller nums1[i]
                // Also ensure i never overtakes j
                i++;
                if (i > j) j = i;
            }
        }

        return maxDist;
    }
};