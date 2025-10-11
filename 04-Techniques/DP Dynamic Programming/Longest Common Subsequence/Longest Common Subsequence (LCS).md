---
Project: Technique
Sites:
BackLinks:
OS compatibility:
Note:
  - LCS
tags:
Created: 2025-08-13
Updated: 2025-08-27
---
# Longest Common Subsequence
---
- LCS vs [[78. Subsets]]
	- LCS = order matter
	- Subset = order doesn't matter

```python 
# Time: O(n * m), Space: O(n + m)
def dp(s1, s2):
    N, M = len(s1), len(s2)
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
	            #                     right       down
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    return dp[N][M]

![[Longest Common Subsequence 2025-08-22 11.52.24.excalidraw]]
