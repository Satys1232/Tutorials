from collections import deque
class Solution:
    def findOrder(self, words: list[str]) -> str:
        adj_list = [[] for _ in range(26)]
        present = [False] * 26
        for word in words:
            for ch in word:
                present[ord(ch) - ord('a')] = True
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            found_difference = False
            for k in range(min(len(first), len(second))):
                if first[k] == second[k]:
                    continue
                from_index = ord(first[k]) - ord('a') 
                to_index = ord(second[k]) - ord('a')
                if to_index not in adj_list[from_index]:
                    adj_list[from_index].append(to_index)
                found_difference = True
                break
            if not found_difference and len(first) > len(second):
                return ""
        V = len(adj_list)
        indegrees = [0] * V
        for node in range(V):
            for neighbor in adj_list[node]:
                indegrees[neighbor] += 1
        queue = deque()
        result = []
        for i in range(V):
            if present[i] and indegrees[i] == 0:
                queue.append(i)
        while len(queue) != 0:
            node = queue.popleft()
            result.append(node)
            for adjNode in adj_list[node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0:
                    queue.append(adjNode)
        if len(result) != sum(present):
            return ""
        return "".join(chr(node + ord('a')) for node in result)

sol = Solution()
words = [
    "baa",
    "abcd",
    "abca" ,
    "cab" ,
    "cad"
]
print(sol.findOrder(words))