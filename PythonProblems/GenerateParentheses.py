class Solution(object):

    def generateParenthesis(self, n):
        list = []

        def recursiveFunc(str, n, open, close):
            if open == n and close == n:
                list.append(str)
            else:
                if open < n:
                    recursiveFunc(str + "(", n, open + 1, close)
                if close < n and close < open:
                    recursiveFunc(str + ")", n, open, close + 1)
        if (n > 0):
            str = ""
            open = 0
            close = 0
            recursiveFunc(str, n, open, close)
        return list

print(Solution().generateParenthesis(3))