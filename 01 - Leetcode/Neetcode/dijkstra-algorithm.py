class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        ed = collections.defaultdict(list)
        t = dict() # { node: shortest distance }
        for i in range(n):
            t[i] = -1

        for u, v, w in edges:
            ed[u].append((v, w))
        minHeap = [(0, src)]
        visit = set()
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in visit:
                continue
            visit.add(n1)
            t[n1] = max(t[n1], w1)

            for n2, w2 in ed[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
                
        return t

print(Solution.shortestPath(3, [[0,1,4]], 0))
