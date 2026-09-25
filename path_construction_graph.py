import heapq
import sys

def shortest_path(n , src ,edges):
    adj_list = [[] for _ in range(n + 1)]
    for u , v , w in edges:
        adj_list[u].append([ v , w])
        adj_list[v].append([ u , w])

    distance = [sys.maxsize for _ in range(n + 1)]
    distance[1] = 0
    parent = [i for i in range(0 , n+1)]
    priority_queue = []
    priority_queue.append((0 , 1))

    while len(priority_queue) != 0:
        dist , node = heapq.heappop(priority_queue)
        for adjNode , weight in adj_list[node]:
            new_d = dist + weight
            if new_d < distance[adjNode]:
                distance[adjNode] = new_d
                heapq.heappush(priority_queue , [new_d , adjNode])
                parent[adjNode] = node
    if distance[n] == sys.maxsize:
        return[-1]
    node = n
    path = []
    while parent[node] != node :
        path.append(node)
        node = parent[node]
    path.append(src)
    path.reverse()
    return path

        
    """
[
    [],
    [[2, 2], [4, 1]],
    [[1, 2], [5, 5], [3, 4]],
    [[2, 4], [4, 3], [5, 1]],
    [[1, 1], [3, 3]],
    [[2, 5], [3, 1]]
]

"""


n = 5 
m = 6 
edges = [[1 , 2 , 2 ] , [2 , 5 , 5 ] ,[2 , 3 , 4] , [ 1 , 4 , 1] , [ 4 , 3 , 3 ] , [3 , 5 , 1]]
print(shortest_path(5 , 1 ,edges))