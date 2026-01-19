class Solution {
public:
    int maxSideLength(vector<vector<int>>& mat, int threshold) {
        int m = mat.size();
        int n = mat[0].size();

        // Prefix sum matrix
        vector<vector<int>> ps(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ps[i + 1][j + 1] =
                    mat[i][j]
                    + ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j];
            }
        }

        // Check if a square of size k is possible
        auto can = [&](int k) {
            for (int i = k; i <= m; i++) {
                for (int j = k; j <= n; j++) {
                    int sum =
                        ps[i][j]
                        - ps[i - k][j]
                        - ps[i][j - k]
                        + ps[i - k][j - k];
                    if (sum <= threshold)
                        return true;
                }
            }
            return false;
        };

        int lo = 0, hi = min(m, n);
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(mid))
                lo = mid;
            else
                hi = mid - 1;
        }

        return lo;
    }
};
