class Solution(object):
    def heightChecker(self, heights):
        sortedheights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != sortedheights[i]:
                count += 1

        return count

print(Solution().heightChecker([1,1,4,2,1,3]))