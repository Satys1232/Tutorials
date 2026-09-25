class Solution:
    def dfs(self , node , result , adj_list , visited, path_visited):
        path_visited[node] = 1
        visited[node] = 1
        for adjNode in adj_list[node]:
            if path_visited[adjNode] == 0 and visited[adjNode] == 0:
                if self.dfs(adjNode , result , adj_list , visited ,path_visited) == True:
                    return True
            elif path_visited[adjNode] == 1:
                return True
        path_visited[node] = 0
        result.append(node)
    def safe_state_list(self , V , edges)->list:
        result = []
        adj_list = [[] for _ in range(V + 1)]
        for u , v in edges:
            adj_list[u].append(v)
        path_visited = [0 for _ in range(V + 1)]
        visited = [0 for _ in range(V + 1)]
        for i in range(1 ,V + 1):
            if visited[i] == 0:
                self.dfs(i , result , adj_list , visited ,path_visited)
        return result if len(result) != 0 else []
'''
# 1 -> [2, 4]
# 2 -> [3]
# 3 -> [1, 4]
# 4 -> [5]
# 5 -> []
# 6 -> [5]
# 7 -> [1]
# 8 -> []

'''
edges = [
    [6, 5],
    [4, 5],
    [3, 4],
    [3, 1],
    [1, 2],
    [2, 3],
    [1, 4],
    [7, 1],
    [9, 5]

]
V = 9
sol = Solution()
res= sol.safe_state_list(V , edges)
sorted_list = sorted(res)
print(sorted_list)


