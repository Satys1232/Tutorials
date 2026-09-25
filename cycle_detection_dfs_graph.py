from collections import deque

# class Solution:
# adj_list = [
#     [],        # node 0
#     [4, 2],    # node 1
#     [1, 3, 6], # node 2
#     [2],       # node 3
#     [1, 5],    # node 4
#     [4, 7],    # node 5
#     [2, 7],    # node 6
#     [5, 6]     # node 7
# ]                 

#         3
#         |
# 1 ----- 2
# |       |
# 4       6
# |       |
# 5 ----- 7

# 0     (isolated)
#     def found_or_not(self , node , parent, adj_list , visited):
#         visited[node] = 1
#         for adjNode in adj_list[node]:
#             if visited[adjNode] == 0:
#                 self.found_or_not(adjNode , node , adj_list , visited)
#             elif adjNode != parent:
#                 return True
#         return False

# V = 8
# visited = [0] * V
# adj_list = [[] for _ in range(V)]
# edges = [
#     [1, 4],
#     [1, 2], 
#     [2, 3],
#     [2, 6],
#     [4, 5],
#     [5, 7],
#     [6, 7]
# ]
# for u , v in edges:
#     adj_list[u].append(v)
#     adj_list[v].append(u)
# is_cycle = Solution()
# print(is_cycle.found_or_not(1 , -1 , adj_list , visited))
class Solution:
    def found_or_not(self, node, parent, adj_list, visited):
        visited[node] = 1
        for adjNode in adj_list[node]:
            if visited[adjNode] == 0:
                if self.found_or_not(adjNode, node, adj_list, visited):
                    return True   # ← no check
            elif adjNode != parent:
                return True
        return False

# ---------- Force the bug ----------
V = 3
adj_list = [
    [1],        # 0 only knows 1
    [0, 2],     # 1 knows 0 and 2
    [1, 0]      # 2 knows 1 and 0  ← the back-edge to 0
]

visited = [0] * V
sol = Solution()

has_cycle = sol.found_or_not(0, -1, adj_list, visited)
print(has_cycle)          # prints False  ← wrong! (there is a cycle)