# Dynamic Programming

[Account Login - LeetCode](https://leetcode.com/explore/learn/card/dynamic-programming/630/an-introduction-to-dynamic-programming/4035/)

[Explore - LeetCode](https://www.evernote.com/shard/s397/sh/841d70fa-6a01-4a0f-82c2-8ca09bafb157/6c2c4da1edb2485a2557ddcb3561e416)

<aside>
💡 Note: Greedy problems have optimal substructure, but not overlapping subproblems

</aside>

[[Divide and Conquer (D&C)]]

# Two way
## #Top-Down
**Memoization, Recursive**(easier to write 🙄), slower

[[509.fibonacci-number_rec.py]]
```python hl:13
class Solution:
    def fib(self, n: int) -> int:
        # rec, memo, top-down: fib(3) -> fib(2) -> fib(1) -> fib(0)
        memo = {0: 0, 1: 1}

        def rec(i):
            if i in memo:
                return memo[i]
            
            memo[i] = rec(i - 1) + rec(i - 2)
            return memo[i]

        return rec(n)
```

## #Top-Down 
**Tabulation, Loop,** faster (no recursion)

[[509.fibonacci-number_loop.py]]
```python hl:8,9,11
class Solution:
    def fib(self, n: int) -> int:
        # loop, btm-up: fib(0) -> fib(1) -> fib(2) -> fib(3)

        if n < 2:
            return n

        fibo = [0] * (n + 1)
        fibo[1] = 1

        for i in range(2, n + 1): # O(n)
            fibo[i] = fibo[i - 1] + fibo[i - 2]

        return fibo[n]
```

Summary:
- #Top-Down  => Recursion, slow
- #Bottom-Up   => Iteration, fast

Comparison
https://medium.com/enjoy-algorithm/top-down-vs-bottom-up-approach-in-dynamic-programming-53b917bfbe0

# When to use
## Example problems
>Asking for <mark style="background: #FF5582A6;">optimum</mark> value, the <mark style="background: #FF5582A6;">number of ways</mark> there are to do something
- What is the minimum cost of doing...
- What is the maximum profit from ...
- How many ways are there to do...
- What is the longest possible...
- Is it possible o reach a certain point...



![[DP 2024-04-30 09.27.20.excalidraw]]