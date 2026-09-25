class Solution:
    def shortest_distance_dfs(self , edges, source , destination):
        V = 9
        adj_list = [[] for _ in range(V)]
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [0 for _ in range(V)]
        min_distance = float("inf")
        def dfs(node , distance):
            nonlocal min_distance
            if node == destination:
                min_distance = min(min_distance , distance)
                return
            for neighbour in adj_list[node]:
                if visited[neighbour] == 0:
                    visited[neighbour] = 1
                    dfs(neighbour , distance +1)
                    visited[neighbour] = 0
        visited[source] = 1
        dfs(source , 0)
        return min_distance if min_distance != float("inf") else -1
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
res = sol.shortest_distance_dfs(edges , 0 , 6)
print(res)
