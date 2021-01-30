class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        counter = [0] * n

        for i in range(n):
            counter[nums[i]-1] += 1

        notinNums = []

        for i in range(n):
            if counter[i] == 0:
                notinNums.append(i + 1)

        return notinNums

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
