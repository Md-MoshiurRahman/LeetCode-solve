class Solution(object):
    def longestCommonPrefix(self, strs):
        strlens = []
        for s in strs:
            strlens.append(len(s))
        i = 0
        longPrefix = ""
        if len(strs) == 0:
            return longPrefix
        elif len(strs) == 1:
            return strs[0]
        else:
            while i < min(strlens):
                flag = 0
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        flag = 1
                        break
                if flag == 0:
                    longPrefix += strs[0][i]
                else:
                    break

                i += 1
            return longPrefix



print(Solution().longestCommonPrefix(["dog","racecar","car"]))
