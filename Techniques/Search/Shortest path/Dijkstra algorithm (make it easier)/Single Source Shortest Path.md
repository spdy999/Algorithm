# Single Source Shortest Path

1. Make all vertices as unvisited initially.
2. Make all nodes with ${\infty}$ distance initially except source node.
3. Repeat the following for (v-1) times: v=vertex numbers
    1. Pick the min. value node which is unprocessed.
    2. mark traversed node as processed $(u ->v)$
    3. update all adjacent vertices

# Complexity

- Time complexity
    - Using a binary heap, $O((|E|+|V|)log(|V|))$
- Space Complexity
    - Using a binary heap, $O(|V|)$
    - Up to $|V|$ vertices may have to be stored