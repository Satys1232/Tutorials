class Solution:
    def dfs(self , node ,  path_visited , adjacency_list):
        path_visited[node] = 1
        for adjNode in adjacency_list[node]:
            if path_visited[adjNode] == 0:
                if self. dfs(adjNode ,path_visited , adjacency_list) == True:
                    return True
            elif path_visited[adjNode] == 1:
                return True
        path_visited[node] = 0 
        return False 
    def is_cyclic(self ,vertex , path_visited , adjacency_list):
        for i in range(1 , vertex + 1):
            if path_visited[i] == 0:
                if self.dfs(i , path_visited , adjacency_list) == True:
                    return True
        return False
vertex = 10
adjacency_list = [[] for _ in range(vertex+1)]
edges = [
    (1, 2),
    (2, 3),
    (2, 8),
    (3, 4),
    (3, 7),
    (4, 6),
    (5, 4),
    (7, 5),
    (8, 9),
    (9, 10),
    (10, 8)
]
for u , v in edges:
    adjacency_list[u].append(v)
path_visited = [0 for _ in range(vertex + 1)]
sol = Solution()
print(sol.is_cyclic(vertex , path_visited , adjacency_list))