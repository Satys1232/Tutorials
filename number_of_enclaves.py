class Solution:
    def dfs(self, r, c, visited, rows, cols, land):
        # Stop if outside the grid
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        # Stop if water or already visited
        if land[r][c] == 0 or visited[r][c] == 1:
            return

        # Mark boundary-connected land as visited
        visited[r][c] = 1

        # Visit four directions
        self.dfs(r - 1, c, visited, rows, cols, land)
        self.dfs(r + 1, c, visited, rows, cols, land)
        self.dfs(r, c - 1, visited, rows, cols, land)
        self.dfs(r, c + 1, visited, rows, cols, land)

    def number_of_enclaves(self, land):
        rows = len(land)
        cols = len(land[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # Top row
        r = 0

        for c in range(cols):
            if land[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r, c, visited, rows, cols, land)

        # Bottom row
        r = rows - 1

        for c in range(cols):
            if land[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r, c, visited, rows, cols, land)

        # Left column
        c = 0

        for r in range(rows):
            if land[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r, c, visited, rows, cols, land)

        # Right column
        c = cols - 1

        for r in range(rows):
            if land[r][c] == 1 and visited[r][c] == 0:
                self.dfs(r, c, visited, rows, cols, land)

        # Count land that was NOT reached from a boundary
        count = 0

        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 and visited[r][c] == 0:
                    count += 1

        return count


land = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

sol = Solution()

res = sol.number_of_enclaves(land)

print(res)