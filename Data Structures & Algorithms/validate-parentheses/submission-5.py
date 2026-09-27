class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        
        stack=[]
        for i in s:
            if i=="(":
                stack.append(")")
            elif i=="[":
                stack.append("]")
            elif i=="{":
                stack.append("}")
            elif not stack or i!=stack[-1]:
                return False
            else:
                stack.pop()
            
        return True if not stack else False

            

