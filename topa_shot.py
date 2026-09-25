class Solution:
    def __init__(self , stack):
        self.stack = stack
    def dfs(self , node , visited , adjacency_list):
        visited[node] = 1
        for adjNode in adjacency_list[node]:
            if visited[adjNode] == 0:
                self.dfs(adjNode , visited , adjacency_list)
        self.stack.append(node)
        
    def topologicl_sort(self , vertex , edges ) -> list:
        visited = [0 for _ in range(vertex + 1)]
        adjacency_list = [[] for _ in range(vertex + 1)]
        for u , v in edges:
            adjacency_list[u].append(v)
        for i in range(vertex):
            if visited[i] == 0:
              self.dfs(i , visited , adjacency_list)
        return self.stack[::-1]
    
if __name__ == "__main__":
    vertex = 4
    edges = [
        (2, 1),
        (3, 4),
        (4, 1)
    ]
    sol = Solution([])
    topo_sorted_list = sol.topologicl_sort(vertex , edges)
    print(topo_sorted_list)