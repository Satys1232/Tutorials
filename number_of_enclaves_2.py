# BFS VERSION.

from collections import deque
class Enclaves:
    def find_enclaves(self , land):
        queue = deque()
        rows = len(land)
        cols = len(land[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows - 1 or c == cols -1:
                    if land[r][c] == 1:
                        queue.append([r , c])
                        visited[r][c] = 1
        while len(queue) != 0:
            x , y = queue.popleft()
            for lx , ly in [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]:
                new_x , new_y = x + lx , y + ly
                if new_x < 0 or new_x >= rows or new_y < 0 or new_y >= cols:
                    continue    
                if visited[new_x][new_y] == 1:
                    continue
                if land[new_x][new_y] == 1:
                    visited[new_x][new_y] = 1
                    queue.append([new_x , new_y])

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
sol = Enclaves()
result = sol.find_enclaves(land)
print(result)



        
























land = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
