from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:

        if n - 1 > len(connections):
            return -1

        def dfs(node, graph, visited):
            visited.add(node)
            for adj in graph[node]:
                if adj in visited:
                    continue
                dfs(adj, graph, visited)

        graph = defaultdict(list)
        for src, dst in connections:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        connected = 1
        for i in range(n):
            if i not in visited:
                dfs(i, graph, visited)
            else:
                connected += 1

        return n - connected

