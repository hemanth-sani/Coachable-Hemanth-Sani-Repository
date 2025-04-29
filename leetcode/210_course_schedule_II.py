from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        visited = [0] * numCourses
        result = []
        has_cycle = False

        for a,b in prerequisites:
                dic[a].append(b)

        def dfs(course):
            nonlocal has_cycle
            if visited[course] == 1:
                has_cycle = True
                return
            if visited[course] == 2:
                return

            visited[course] = 1
            for pre in dic[course]:
                dfs(pre)
                if has_cycle:
                    return []
            
            visited[course] = 2
            result.append(course)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
                if has_cycle:
                    return []

        return result
