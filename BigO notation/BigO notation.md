# BigO notation

[https://www.youtube.com/watch?v=__vX2sjlpXU](https://www.youtube.com/watch?v=__vX2sjlpXU)

- complexity in terms of **input size**, N
- machine-**independent**

# Types of measurement

- **worst - case**
- best - case
- average - case

# General rules

- ignore constant
    - `5n -> O(n)`
- certain terms “dominate” others
    - `O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!)`
        
        ![Untitled](BigO%20notation/Untitled.png)
        
    - ignore **low-order** term
    
    # Example
    
    ## Constant time
    
    **independent** of input size, N
    
    $x = 5+(15*20)$
    
    `**O(1)`** 
    
    $x=5+(15*20)$
    
    $y=15-2$
    
    print(x + y)
    
    `total time = O(1) + O(1) + O(1) = 3 * O(1) = **O(1)**`
    
    ## Linear time
    
    ```python
    for x in range(N):
    	print(x) # O(1)
    **# N * O(1) = O(N)**
    ```
    
    ```python
    y = 5 + (15 * 20) # O(1)
    
    ############################
    for x in range(N):
    	print(x)
    **# N * O(1) = O(N)**
    ############################
    ```
    
    `total time = O(1) + O(N) = O(N)`
    
    - dominate rule
    
    ## Quadratic time
    
    ```python
    for x in range(N): # N * O(N) = **O(N^2)          ^**
    	for y in range(N): # N * O(1) = O(N)          |
    		print(x * y) # O(1)                         |
    ```
    
    `total time =  O(N^2)`
    
    ```python
    x = 5 + (15 * 20) # O(1)
    
    for x in range(N): # N * O(1) = O(N)
    	print(x) # O(1)
    
    for x in range(N): # N * O(N) = **O(N^2)**
    	for y in range(N): # O(N)
    		print(x * y) # O(1)
    ```
    
    `total time = O(1) + O(N) + O(N^2) = O(N^2)`
    
    - dominate rule

# Conditional calculation

`O(?)`

```python
if x > 0:
	# O(1)
elif x < 0:
	# O(logN)
else:
	# O(N^2)
```

- Need choose the **largest** one ⇒ `O(N^2)`

# Real world

- Constant matter
- be cognizant of **best-case** and **average-case**

# TODO:

BigO for Tree