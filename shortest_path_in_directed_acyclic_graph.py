class Solution:
    def dfs(self ,node , stack , visited , adj_list):

        visited[node] = 1

        for adjNode , dist in adj_list[node]:
            if visited[adjNode] == 0:
                self.dfs(adjNode , stack , visited , adj_list)
                
        stack.append(node)

    def shortestPath(self , V , edges):
        adj_list = [[] for _ in range(V)]
        for u , v , d in edges:
            adj_list[u].append([v , d])

        stack = [] 
        visited = [0 for _ in range(V)]

        for i in range(V):
            if visited[i] == 0:
                self.dfs(i , stack , visited , adj_list) 

        distance =[float("inf") for _ in range(V)]
        distance[0] = 0

        while len(stack) != 0:
            node = stack.pop()
            dist = distance[node]
            for adjNode , d in adj_list[node]:
                new_d = dist + d
                distance[adjNode] = min(distance[adjNode] , new_d)
        
        for i in range(0 , V):
            if distance[i] == float("inf"):
                distance[i] = -1
        return distance

V = 6
edges = [[0,1,2], [0,4,1], [4,5,4], [4,2,2], [1,2,3], [2,3,6], [5,3,1]] 
sol = Solution()
shortest_paths = sol.shortestPath(V , edges)
print(shortest_paths)