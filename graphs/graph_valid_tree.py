from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # build graph
        graph_map = defaultdict(list)
        for u, v in edges:
            graph_map[u].append(v)
            graph_map[v].append(u)

        visited = [False] * n # to check connectivity

        def has_cycle(node, parent):
            visited[node] = True
            for nei in graph_map[
                node]:  # Accessing here creates keys safely because we aren't looping 'graph_map' outside
                if nei == parent:
                    continue
                if visited[nei]:
                    return True
                if has_cycle(nei, node):
                    return True
            return False

        # Run DFS only once from node 0
        if has_cycle(0, -1):
            return False

        # Check connectivity
        if not all(visited):
            return False

        return True



