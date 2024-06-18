# Heap

- Heap is a **special** type of **[[binary tree]]**
- A [[complete binary tree]]
    
    
    ![[/Untitled.png]]


## Max heap
Every parent is **≥** to its children
## Min heap
Every parent is **≤** its children

- The **maximum** or **minimum** value will always be at the root of the tree - the advantage of using a heap
- Time complexity
    
    ![Untitled](Heap/Untitled%201.png)
    
    - **heapify : $O(N)$**
    - **insert** : $O(log(n))$
    - **delete** (without index) :
        - worse case : $O(n log(n))$
            - $n :$ for linear search
            - $log(n):$ for fix the heap
        - root : $O(log(n))$
            - no search ⇒ no $n$

[Heap queue (or heapq) in Python - GeeksforGeeks](https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/)

[[Priority Queues]]

[[Heaps - Sort]]

# Application of Heap

1. Heap sort
2. The **Top-K** problem
3. the K-th element