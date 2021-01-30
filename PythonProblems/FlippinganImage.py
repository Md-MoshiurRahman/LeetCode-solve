class Solution(object):
    def flipAndInvertImage(self, nums):
        for i in range(len(nums)):
            nums[i].reverse()
            for j in range(len(nums)):
                if nums[i][j]==1:
                    nums[i][j] = 0
                else:
                    nums[i][j] = 1

        return nums

print(Solution().flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))