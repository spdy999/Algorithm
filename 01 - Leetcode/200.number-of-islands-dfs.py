class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time complexity: O(rows * cols)
        # Space complexity: O(rows * cols)
        
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        drs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if not (0 <= r < rows) or \
                not (0 <= c < cols) or \
                grid[r][c] != '1':
                return
            
            grid[r][c] = '0'

            [dfs(r + dr, c + dc) for dr, dc in drs]
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    cnt += 1
        
        return cnt