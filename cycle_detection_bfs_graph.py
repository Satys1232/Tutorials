from collections import deque

class Solution:
#      adj_list = [
#      [1, 2],      # node 0
#      [0, 2],      # node 1
#      [0, 1, 3],   # node 2
#      [2]          # node 3
#      ]
    def found_or_not(self , V , edges):
        queue = deque()
        adj_list = [[] for _ in range(V)]
        for u , v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [0] * V
        #--------------------------
        for i in range( 0 , V):
            if visited[i] == 1:
                continue
            queue.append((i , -1))
            visited[i] = 1
            while queue:
                node , parent = queue.popleft()
                for adjNode in adj_list[node]:
                    if visited[adjNode] == 0:
                        visited[adjNode] = 1
                        queue.append((adjNode , node))
                    else :
                        if adjNode != parent:
                            return True

        return False

V = 4
edges = [
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 3]
]
is_cycle = Solution()
print(is_cycle.found_or_not(V , edges))