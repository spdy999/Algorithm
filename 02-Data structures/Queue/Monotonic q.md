## Description
### GPT 4 summary
A monotonic queue is a <mark style="background: #FFB86CA6;">data structure</mark> similar to a regular queue but maintains its elements in a <mark style="background: #FF5582A6;">sorted order</mark>, either <mark style="background: #FFB86CA6;">non-increasing</mark>( #Decreasing ) or <mark style="background: #FFB86CA6;">non-decreasing</mark>( #Increasing ). This sorting allows for fast retrieval of the minimum or maximum element, ideal for problems like identifying extremities within a [[Sliding Window|Sliding Window]] across a dataset. It typically utilizes a [[Deque]] (double-ended queue) to efficiently add and remove items while preserving order.
- Seems like this is refer to [[239. Sliding Window Maximum]]


## #Increasing (aka. Non-decreasing)

![[Monotonic q.png]]
## #Decreasing (aka. Non-increasing)

![[Monotonic q-1.png]]


---
## TLDR
- Non monotonic
![[Monotonic q-2.png]]


