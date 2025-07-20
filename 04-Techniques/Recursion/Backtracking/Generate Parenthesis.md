# Generate Parenthesis

![[Generate Parenthesis.jpg]]


```python
# https://www.youtube.com/watch?v=s9fokUqJ76A&ab_channel=NeetCode
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if open >= close
        # valid IIF open == close == n

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)

        return res
```