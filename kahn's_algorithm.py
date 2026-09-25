# '''       3
#         /   \
#        .     .
#        1     5
#        .     .
#        |     |
#        4     2
#        .     .
#        \     /
#           6
# '''
from collections import deque
class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list:
        indegrees = [0 for _ in range(V)]
        adjacency_list = [[] for _ in range(V)]
        queue = deque()
        result = []
        for u , v in edges:
            adjacency_list[u].append(v)
            indegrees[v] += 1
        for i in range(V):
            if indegrees[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            e = queue.popleft()
            result.append(e)
            for adjNode in adjacency_list[e]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        return result if len(result) == V else []
sol = Solution()
V = 7
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    # [3, 1],  # Creates a cycle: 1 -> 2 -> 3 -> 1
    [3, 4],
    [4, 5],
    [5, 6]
]
print(sol.topoSort(V, edges))

    
                
                
            
            
                
        
        


