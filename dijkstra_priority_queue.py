import heapq
class Solution:
    def dijkstra(self , V , edges , src):
        adj_list = [[] for _ in range(V)]
        for u , v , d in edges:
            adj_list[u].append([v ,d])
        distance = [float("inf") for _ in range(V)]
        distance[src] = 0
        priority_queue = [[distance[src] , src]]
        while len(priority_queue) != 0:
            curr_dist , node  = heapq.heappop(priority_queue)
            if curr_dist > distance[node]:
                continue
            for adjNode , weight in adj_list[node]:
                dist_trav = curr_dist + weight
                if dist_trav < distance[adjNode]:
                    distance[adjNode] = dist_trav
                    priority_queue.append([dist_trav , adjNode])
        return distance

