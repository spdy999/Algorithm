/*
 * @lc app=leetcode id=70 lang=cpp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
class Solution
{
public:
    map<int, int> memo;
    int fib(int n)
    {
        if (n == 1)
            return memo[1];
        if (n == 2)
            return memo[2];

        if (memo[n] > 0)
        {
            // cout << "!!!Memo: " << memo[n] << endl;
            return memo[n];
        }

        memo[n] = fib(n - 2) + fib(n - 1);
        // for (int i = n; i > 0; i--)
        // {
        //     cout << "Memo " << i << ": " << memo[i] << " ";
        // }
        // cout << endl;

        return memo[n];
    }

    int climbStairs(int n)
    {
        // memoization(using map), Top-down
        memo[1] = 1;
        memo[2] = 2;
        return fib(n);
    }
};
// @lc code=end
