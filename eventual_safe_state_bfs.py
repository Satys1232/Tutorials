from collections import deque
class Solution:
    def eventualSafeNodes(self , graph:list[list[int]]) -> list[int]:
        V = len(graph)
        # Reversing Adjacency List
        adj_list = [[] for _ in range(V)]
        for node in range(V):
            for adjNode in graph[node]:
                adj_list[adjNode].append(node)

        queue = deque()
        # Calculate indegrees:
        indegrees = [0 for _ in range(V)]
        for node in range(len(adj_list)):
            for adjNode in adj_list[node]:
                indegrees[adjNode] += 1

        # Add all the nodes with indegree 0 in queeue
        for node in range(0 , V):
            if indegrees[node] == 0:
                queue.append(node)

        result = []
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node)
            for adjNode in adj_list[node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
                    
        result.sort()
        return result

graph  = [
    [1],        # 0 → 1
    [2, 4],     # 1 → 2, 1 → 4
    [0],        # 2 → 0
    [2],        # 3 → 2
    [6],        # 4 → 6
    [4],        # 5 → 4
    [7, 11],    # 6 → 7, 6 → 11
    [8, 11],    # 7 → 8, 7 → 11
    [10],       # 8 → 10
    [],         # 9 has no outgoing edges
    [9],        # 10 → 9
    [10]        # 11 → 10
]

sol = Solution()
res = sol.eventualSafeNodes(graph)
print(res)