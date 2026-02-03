class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();
        int i = 0;

        // 1) strictly increasing
        while (i + 1 < n && nums[i] < nums[i + 1]) {
            i++;
        }
        // need at least one increase and not reach the end
        if (i == 0 || i == n - 1) return false;

        // 2) strictly decreasing
        while (i + 1 < n && nums[i] > nums[i + 1]) {
            i++;
        }
        // need at least one decrease and not reach the end
        if (i == n - 1) return false;

        // 3) strictly increasing again
        while (i + 1 < n && nums[i] < nums[i + 1]) {
            i++;
        }

        // must consume the whole array
        return i == n - 1;
    }
};
