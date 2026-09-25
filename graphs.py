# n = 5
# m = 6
# edges = [[1 , 2]  ,[2 , 4] , [3 , 4] , [1 , 3] , [3 , 5] , [5 , 4]]
    
    #     GRAPH

    #       1
    #      / \
    #     /   \
    #    2     3
    #     \   / \
    #      \ /   \
    #       4 - - 5

# ---------- USING MATRIX ----------

# matrix = [[0 for _ in range(n+1)] for _ in range(n + 1) ]
# def print_matrix(matrix):
#     n = len(matrix)
#     print("    ", end="")
#     for col in range(n):
#         print(col, end="  ")
#     print()
#     for row in range(n):
#         print(f"{row}  {matrix[row]}")

# for u,v in edges:
#     matrix[u][v] = 1
#     matrix[v][u] = 1

# print(matrix)

#    0  1  2  3  4  5                                  
# 0  [0, 0, 0, 0, 0, 0]
# 1  [0, 0, 1, 1, 0, 0]
# 2  [0, 1, 0, 0, 1, 0]
# 3  [0, 1, 0, 0, 1, 1]    
# 4  [0, 0, 1, 1, 0, 1]
# 5  [0, 0, 0, 1, 1, 0]

# ---------- USING MATRIX ----------

# ---------- USING LIST ----------

# lst = [[] for _ in range(n+1)]
# for u , v in edges:
#     lst[u].append(v)
#     lst[v].append(u)
# print(lst)

# [[], [2, 3], [1, 4], [4, 1, 5], [2, 3, 5], [3, 4]]

# ---------- USING LIST ----------

# ---------- USING DICTIONARY ----------
# my_dict = {}
# for i in range(1 , n+1):
#     my_dict[i] = []

# for u , v in edges:
#     my_dict[u].append(v)
#     my_dict[v].append(u)

# print(my_dict)

# ---------- USING DICTIONARY ----------

# from collections import deque

# n = 8
# adjacency_list = [
#     [] , #0
#     [2 , 4] ,  #1
#     [1 , 3 , 6] , #2
#     [2] , #3
#     [1  , 5 , 7] , #4
#     [4 , 8] , #5 
#     [2] , #6
#     [4 , 8] , #7
#     [5 , 7], #8
# ]
# Bfs ----------------------------------
# def bfs(n , adj , start_node):
#     ans = []
#     queue = deque()
#     visited = [0] * (n + 1)
#     queue.append(start_node)
#     visited[start_node] = 1
#     while len(queue) != 0:
#         e = queue.popleft()
#         ans.append(e)
#         for node in adj[e]:
#             if visited[node] == 0:
#                 queue.append(node)
#                 visited[node] = 1 
#     return ans
# print(bfs(n , adjacency_list ,1))

# Bfs -------------------------------------

# def dfs(adj , start , ans , visited):
#     ans.append(start)
#     visited[start] = 1
#     for e in adj[start]:
#         if visited[e] == 0:
#             dfs(adj , e , ans , visited)
#     return ans

# visited = [0] * (n + 1)
# print(dfs(adjacency_list , 1 , [] , visited ))

# Bfs ---------------------------------------

# Rotten oranges -----------------

# from copy import deepcopy
# from collections import deque
# class Orange:
#     def __init__(self):
#         pass
#     def orangesRotting(self , grid: list[list[int]]) -> int:
#         rows = len(grid)
#         cols = len(grid[0])
#         grid_copy = deepcopy(grid)

#         fresh_cnt = 0
#         queue = deque()

#         for r in range(rows):
#             for c in range(cols):
#                 if grid_copy[r][c] == 2:
#                     queue.append((r , c))
#                 elif grid_copy[r][c] == 1:
#                     fresh_cnt += 1
#         minutes = 0
#         while len(queue) != 0 and fresh_cnt > 0:
#             minutes += 1
#             total_rotten = len(queue)
#             for _ in range(total_rotten):
#                 i , j = queue.popleft()
#                 for dx , dy in [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]:
#                     new_i , new_j = i + dx , j + dy
#                     if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
#                         continue
#                     if grid_copy[new_i][new_j] == 0 or \
#                         grid_copy[new_i][new_j] == 2:
#                         continue
#                     fresh_cnt -= 1
#                     grid_copy[new_i][new_j] == 2
#                     queue.append((new_i , new_j))
#         if fresh_cnt > 0:
#             return -1
#         return minutes
    

# Rotten oranges -----------------
            

# from copy import deepcopy
# from collections import deque
# class FloodFill:
#     def __init__(self):
#         pass
#     def flood(self , grid: list[list[int]] , row , col , color) -> list[list[int]]:

#         if grid[row][col] == color:
#             return grid

#         to_change = grid[row][col]
        
#         rows = len(grid)
#         cols = len(grid[0])
#         grid_copy = deepcopy(grid)
#         queue = deque()
#         queue.append((row , col))
#         grid_copy[row][col] = color

#         while len(queue) != 0 :
#             total_flooded = len(queue)
#             for _ in range(total_flooded):
#                 i , j = queue.popleft()
#                 for dx , dy in [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]:
#                     new_i , new_j = i + dx , j + dy 
#                     # calculated nwe_i and new_j
#                     if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
#                         continue
#                     if grid_copy[new_i][new_j] == to_change:
#                         grid_copy[new_i][new_j] = color
#                         queue.append((new_i , new_j))

#         return grid_copy
# 
# grid=[
#     [2,1,0,1,1],
#     [1,1,0,1,0],
#     [0,1,1,1,0],
#     [0,0,1,0,1]
# ]

# flood_fill = FloodFill()
# result=flood_fill.flood(grid , 1 , 1 , 5)

# for row in result:
#     print(*row)

# from copy import deepcopy
# from collections import deque
# class FloodFill:
#     def __init__(self):
#         pass
#     def flood(self , grid: list[list[int]] , grid_copy: list[list[int]] ,  row , col , color) -> list[list[int]]:
#         rows = len(grid)
#         cols = len(grid[0])
#         element = grid[row][col]
#         grid_copy[row][col] = color

#         for dx , dy in [(1 , 0) , (-1 , 0) , (0 , 1) , (0 , -1)]:
#             new_i , new_j = row + dx , col + dy 
#             if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
#                 continue
#             if grid_copy[new_i][new_j] == element:
#                 grid_copy[new_i][new_j] = color
#                 self.flood(grid ,grid_copy, new_i , new_j , color)

#         return grid_copy

# grid=[
#     [2,1,0,1,1],
#     [1,1,0,1,0],
#     [0,1,1,1,0],
#     [0,0,1,0,1]
# ]

# grid_copy = deepcopy(grid)

# flood_fill = FloodFill()

# result = flood_fill.flood(grid , grid_copy , 1 , 1 , 5)

# for row in result:
#     print(*row)