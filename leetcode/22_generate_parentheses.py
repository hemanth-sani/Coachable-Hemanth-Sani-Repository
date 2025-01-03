class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def parenthesisFormation(open_count, close_count):

            if open_count == close_count == n:
                res.append("".join(stack))
            
            if open_count < n:
                stack.append("(")
                parenthesisFormation(open_count + 1, close_count)
                stack.pop()
            
            if close_count < open_count:
                stack.append(")")
                parenthesisFormation(open_count, close_count + 1)
                stack.pop()
        
        parenthesisFormation(0,0)
        return res
