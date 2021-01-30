from _collections import deque

class Solution(object):
    def letterCombinations(self, str):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        result = []
        stack = deque()
        stack.append("")
        length = len(str)

        while len(stack) != 0:
            s = stack.pop()
            if len(s)==length:
                if s!="":
                    result.append(s)
            else:
                for letter in phone[str[len(s)]]:
                    stack.append(s+letter)


        return result
            



print(Solution().letterCombinations(""))