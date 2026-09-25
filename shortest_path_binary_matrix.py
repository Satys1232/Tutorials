from collections import deque
def shortest_path_matrix():
    steps = 1
    matrix = [
        [0 , 1 , 1 , 1] ,
        [0 , 0 , 1 , 0] ,
        [0 , 0 , 1 , 0] ,
        [0 , 1 , 0 , 1] ,
        [0 , 0 , 0 , 1] ,
    ]
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    queue.append([0 , 0])
    visited[0][0] = 1
    while len(queue) != 0:
        size = len(queue)
        for _ in range(size):
            r , c = queue.popleft()
            for x , y in [(1 , 0) , (-1 , 0) ,(0 , -1) , (0 , 1) , (-1 , 1) , (-1 , -1 ) , (1 , -1) , (1 , 1)]:
                new_r , new_c = r + x , c + y
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if new_r == 3 and new_c == 2:
                    return steps + 1
                if visited[new_r][new_c] == 0:
                    if matrix[new_r][new_c] == 0:
                        visited[new_r][new_c] = 1
                        queue.append([new_r , new_c])
        steps += 1            
    return -1
print(shortest_path_matrix())