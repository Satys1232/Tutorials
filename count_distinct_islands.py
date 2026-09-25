class Solution:
    def dfs(self , r , c , base_r , base_c , rows , cols , grid , shape , visited):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or visited[r][c] == 1:
            return shape
        visited[r][c] = 1
        shape.append((r - base_r , c - base_c))
        self.dfs(r + 1, c , base_r , base_c , rows , cols , grid , shape , visited)
        self.dfs(r -1 , c , base_r , base_c , rows , cols , grid , shape , visited)
        self.dfs(r , c +1 , base_r , base_c , rows , cols , grid , shape , visited)
        self.dfs(r , c- 1 , base_r , base_c , rows , cols , grid , shape , visited)
        return shape
    def count_distinct_islands(self , grid) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        unique_islands = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if visited[r][c] == 0:
                        shape = []
                        unique_islands.add(tuple(self.dfs(r , c , r , c , rows , cols , grid ,shape , visited)))
        return(len(unique_islands))

sol = Solution()
grid = [
    [1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1]
]
result = sol.count_distinct_islands(grid)
print("Number of distinct Islands are : " , result)

