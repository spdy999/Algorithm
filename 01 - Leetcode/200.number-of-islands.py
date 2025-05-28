#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid[0]) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0
        drs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()

        def addGrid(r, c):
            # in range, interested ('1'), not in visited
            if (r >=0 and r < rows and
            c >= 0 and c < cols and
            grid[r][c] == '1' and
            (r, c) not in visited):
                q.append((r, c))            

        def bfs(r: int, c: int):
            q.append((r, c))
            while q:
                cr, cc = q.pop()                
                visited.add((cr, cc))
                # print('q:', q)
                # print('visited:', visited)
                for drr, drc in drs:
                    addGrid(cr + drr, cc + drc)
            
        # O(m * n)
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell == '1' and (r, c) not in visited:
                    q.append((r, c))
                    bfs(r, c)
                    count += 1
        return count
        
# @lc code=end

