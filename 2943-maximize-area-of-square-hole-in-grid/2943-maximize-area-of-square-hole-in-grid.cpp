class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        auto getMaxGap = [&](vector<int>& bars) {
            sort(bars.begin(), bars.end());
            int longest = 1, curr = 1;

            for (int i = 1; i < bars.size(); i++) {
                if (bars[i] == bars[i - 1] + 1)
                    curr++;
                else
                    curr = 1;
                longest = max(longest, curr);
            }
            return longest + 1;  // gap size
        };

        int maxH = getMaxGap(hBars);
        int maxV = getMaxGap(vBars);

        int side = min(maxH, maxV);
        return side * side;
    }
};