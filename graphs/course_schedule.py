from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adj = {i: [] for i in range(numCourses)}
        in_degree: list[int] = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] +=1

        # 3. Add courses with NO prerequisites to queue (starting points)
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while q:
            course = q.popleft()
            result.append(course)

            for nei in adj[course]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)

        return result if len(result) == numCourses else []