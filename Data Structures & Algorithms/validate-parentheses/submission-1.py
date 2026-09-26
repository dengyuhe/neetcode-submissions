class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        for sym in s:
            if sym=="{":
                stack.append("}")
            elif sym=="[":
                stack.append("]")
            elif sym=="(":
                stack.append(")")
            elif not stack or stack[-1]!=sym:
                return False
            else:
                stack.pop()

        return True if not stack else False

            

