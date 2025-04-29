class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def parenthesis_formation(open_count, close_count):

            if open_count == close_count == n:
                res.append("".join(stack))
            
            if open_count < n:
                stack.append("(")
                parenthesis_formation(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(")")
                parenthesis_formation(open_count, close_count + 1)
                stack.pop()
        
        parenthesis_formation(0,0)
        return res
