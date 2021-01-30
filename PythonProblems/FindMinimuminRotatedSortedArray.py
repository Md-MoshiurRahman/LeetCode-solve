class Solution(object):
    def findMin(self, nums):
        nums.sort()
        return nums[0]

print(Solution().findMin([3,4,5,1,2]))
