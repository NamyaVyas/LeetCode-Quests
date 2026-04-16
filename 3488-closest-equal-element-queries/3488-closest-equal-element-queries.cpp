class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        int m = n * 2;

        // d[i] = min distance from index i (in doubled array) to nearest same-value element
        vector<int> d(m, m);

        // Left pass: for each position, check the most recent occurrence of nums[i % n]
        unordered_map<int, int> left;
        for (int i = 0; i < m; i++) {
            int x = nums[i % n];
            if (left.count(x)) {
                d[i] = min(d[i], i - left[x]);
            }
            left[x] = i;
        }

        // Right pass: for each position, check the next occurrence of nums[i % n]
        unordered_map<int, int> right;
        for (int i = m - 1; i >= 0; i--) {
            int x = nums[i % n];
            if (right.count(x)) {
                d[i] = min(d[i], right[x] - i);
            }
            right[x] = i;
        }

        // Merge: d[i] in original range gets the best of itself and its mirror in the second half
        for (int i = 0; i < n; i++) {
            d[i] = min(d[i], d[i + n]);
        }

        // Answer queries
        vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            ans.push_back(d[q] >= n ? -1 : d[q]);
        }
        return ans;
    }
};