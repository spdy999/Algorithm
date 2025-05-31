/*
 * @lc app=leetcode id=5 lang=cpp
 *
 * [5] Longest Palindromic Substring
 */

// @lc code=start
// https://www.youtube.com/watch?v=XYQecbcd6_c&ab_channel=NeetCode
class Solution
{
public:
    string lgp = "";
    string checkLpd(int il, int ir, int lenPd, string s)
    {
        int n = s.size();
        while (il >= 0 && ir < n && s[il] == s[ir]) // O(n)
        {
            lenPd = ir - il + 1;
            if (lenPd > lgp.size())
            {
                lgp = string(&s[il], &s[ir + 1]);
            }
            il--;
            ir++;
        }
        return lgp;
    }

    string longestPalindrome(string s)
    {
        int n = s.size();

        // O(n^2)
        for (int i = 0; i < n; i++) // O(n)
        {
            // odd length
            lgp = checkLpd(i, i, 1, s);

            // even length
            lgp = checkLpd(i, i + 1, 1, s);
        }
        return lgp;
    }
};
// @lc code=end
