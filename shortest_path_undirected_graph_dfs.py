from collections import deque
class Solution:
    def shortest_path_bfs(self ,edges , vertex , src):
        adj_list = [[] for _ in range(vertex)]
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        distance = [-1 for _ in range(vertex)]
        distance[src] = 0
        queue = deque()
        queue.append((src , 0))
        while len(queue) != 0:
            node  , dist = queue.popleft()
            for adjNode in adj_list[node]:
                if distance[adjNode] == -1:
                    distance[adjNode] = dist  + 1
                    queue.append((adjNode , dist + 1))
        return distance
vertex = 9
edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 4),
    (2, 3),
    (3, 5),
    (4, 6),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8)
]
sol = Solution()
print(sol.shortest_path_bfs(edges , vertex , 0))