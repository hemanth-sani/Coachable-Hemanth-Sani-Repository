class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, cur, totle):
            if totle == target:
                curr = cur[:]
                result.append(curr)
                return
                
            if i >= len(candidates) or totle > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, totle + candidates[i])
            cur.pop()
            dfs(i + 1, cur, totle)

        dfs(0, [], 0)
        print(result)

        return result
