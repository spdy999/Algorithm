/*
 * @lc app=leetcode id=647 lang=cpp
 *
 * [647] Palindromic Substrings
 */

// @lc code=start
class Solution
{
public:
    int cnt = 0;
    void checkLpd(int il, int ir, int lenPd, string s)
    {
        int n = s.size();
        while (il >= 0 && ir < n && s[il] == s[ir]) // O(n)
        {
            cnt += 1;

            il--;
            ir++;
        }
    }

    int countSubstrings(string s)
    {
        int n = s.size();

        // O(n^2)
        for (int i = 0; i < n; i++) // O(n)
        {
            // odd length
            checkLpd(i, i, 1, s);

            // even length
            checkLpd(i, i + 1, 1, s);
        }

        return cnt;
    }
};
// @lc code=end
