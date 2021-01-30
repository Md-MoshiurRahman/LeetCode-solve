import operator
class Solution(object):
    def compareVersion(self, version1,version2):
        x1 = version1.split('.')
        x2 = version2.split('.')

        n1 = len(x1)
        n2 = len(x2)

        for i in range(0, n1):
            x1[i] = int(x1[i])

        for i in range(0, n2):
            x2[i] = int(x2[i])

        if n1>n2:
            for i in range(n1-n2):
                x2.append(0)
        if n2>n1:
            for i in range(n2-n1):
                x1.append(0)

        if x1 > x2:
            return 1
        elif x2 > x1:
            return -1
        else:
            return 0



print(Solution().compareVersion("1.01","1.001.0"))
