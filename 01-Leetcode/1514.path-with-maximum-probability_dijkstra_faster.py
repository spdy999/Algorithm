#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        ed = defaultdict(list)
        prob = defaultdict(int)  # {node: maxProb}

        for uv, w in zip(edges, succProb):
            u, v = uv
            ed[u].append((v, w))
            ed[v].append((u, w))

        maxHeap = [(-1, start_node)]
        visit = set()

        while maxHeap:
            w1, n1 = heapq.heappop(maxHeap)

            if n1 in visit:
                continue

            visit.add(n1)
            prob[n1] = min(prob[n1], w1)

            if n1 == end_node:
                return -prob[end_node]

            for n2, w2 in ed[n1]:
                if n2 not in visit:
                    heapq.heappush(maxHeap, (w1 * w2, n2))
        return 0

        
# @lc code=end

