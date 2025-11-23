def iterative_dfs(graph, start_node):
    """
    Performs an iterative DFS on a graph.

    :param graph: Adjacency list (e.g., {'A': ['B', 'C'], ...})
    :param start_node: The node to start the search from
    """

    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            print(current_node)
            visited.add(current_node)

            # 8. Add all *unvisited* neighbors to the stack
            #    We check if the node is in the graph in case it's a
            #    node with no outgoing edges.
            if current_node in graph:
                # We add neighbors in reverse order if we want
                # to match the exploration order of a typical
                # recursive DFS (e.g., always explore 'left' child first).
                # For the simplest structure, the order doesn't matter,
                # but reversing is common practice.
                for neighbor in reversed(graph[current_node]):
                    if neighbor not in visited:
                        stack.append(neighbor)