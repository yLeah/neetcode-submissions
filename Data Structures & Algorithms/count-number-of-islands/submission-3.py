class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # this is dfs solution (stack)
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r,c):
            #check if the current cell is water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            #mark land as visited by sinking it or making it 0
            grid[r][c] = "0"

            # recursively visit all neighbors, down up left right 
            dfs(r, c-1)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r+1, c)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands +=1
                    dfs(r,c)
        return islands 