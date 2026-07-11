class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for st in s:
            if st  == '{' or st == '[' or st == '(':
                stack.append(st)
            else:
                
                if len(stack)==0:
                    return False
                top = stack.pop()
                if st == '}' and top != '{':
                    return False
                elif st == ']' and top != '[':
                    return False
                elif st == ')' and top != '(':
                    return False
        return len(stack) == 0
