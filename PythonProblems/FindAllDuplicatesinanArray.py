class Solution(object):
    def findDuplicates(self, nums):
        n = len(nums)
        nums.sort()
        dup = []

        for i in range(1,n):
            if nums[i - 1] == nums[i]:
                dup.append(nums[i])

        return dup

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
