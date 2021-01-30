from _collections import deque
class Solution(object):
    def isValid(self, str):
        stack = deque()

        for s in str:
            if s=="(" or s=="{" or s=="[":
                stack.append(s)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    if top=="(" and s!=")":
                        return False
                    if top=="{" and s!="}":
                        return False
                    if top=="[" and s!="]":
                        return False

        if len(stack)!= 0:
            return False
        else:
            return True


print(Solution().isValid("("))
