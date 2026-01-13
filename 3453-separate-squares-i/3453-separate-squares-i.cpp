class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double low = 1e18, high = -1e18;
        double totalArea = 0.0;

        for (auto &s : squares) {
            double y = s[1], l = s[2];
            low = min(low, y);
            high = max(high, y + l);
            totalArea += l * l;
        }

        for (int iter = 0; iter < 60; iter++) {  // precision control
            double mid = (low + high) / 2.0;
            double below = 0.0;

            for (auto &s : squares) {
                double y = s[1], l = s[2];
                double bottom = y;
                double top = y + l;

                if (mid <= bottom) {
                    // entirely above
                    continue;
                } else if (mid >= top) {
                    // entirely below
                    below += l * l;
                } else {
                    // cut by line
                    below += (mid - bottom) * l;
                }
            }

            if (below < totalArea - below) {
                low = mid;
            } else {
                high = mid;
            }
        }

        return (low + high) / 2.0;
    }
};
