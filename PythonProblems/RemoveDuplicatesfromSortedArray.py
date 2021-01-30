class Solution(object):
    def removeDuplicates(self, nums):
        count = 1
        base = 0
        i = 1
        while(i<len(nums)):
            if(nums[i]==nums[base]):
                count+=1

            if (nums[i] != nums[base]) or i==len(nums)-1:
                for j in range(1,count):
                    nums.remove(nums[base])
                base += 1
                count = 1
                i = base
            i+=1
        return len(nums)



solution = Solution()
print(solution.removeDuplicates([1,1,1,2,3,3,3,3,3,3]))