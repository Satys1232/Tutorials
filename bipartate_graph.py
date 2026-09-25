class Solution:
    def dfs(self , node , colors , adjList): 
        for adjNode in adjList[node]:
            if colors[adjNode] == 0:
                if colors[node] == "red":
                    colors[adjNode] = "green"
                else:
                    colors[adjNode] = "red"
                if self.dfs(adjNode , colors , adjList) == False:
                    return False
            elif colors[adjNode] == colors[node]:
                return False
        return True
    def is_bipartite(self , vertex , edges) ->bool:
        adjList = [[] for _ in range(vertex)]
        for u , v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        colors = [0 for _ in range(vertex)]
        for i in range(1 ,vertex):
            if colors[i] != 0:
                continue
            colors[i] = "red"
            if self.dfs(i , colors , adjList) == False:
                return False
        return True

if __name__ == "__main__":
    edges = [
        [1, 2],
        [2, 3],
        [2, 11],
        [3, 4],
        [4, 5],
        [5, 6],
        [6, 7],
        [6, 9],
        [7, 8],
        [9, 10],
        [9, 12],
        [10, 11],
        [10, 12]
    ]
    vertex = 13
    sol = Solution()
    print(sol.is_bipartite(vertex , edges))