class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = []
        for i in range(n - 1):

            # Find all pairs with sum
            # equals to "-arr[i]"
            s = set()
            for j in range(i + 1, n):
                x = -(nums[i] + nums[j])
                if x in s:
                    value = sorted([nums[i], nums[j], x])
                    if value not in result:
                        result.append(value)
                else:
                    s.add(nums[j])
        return result



print(Solution().threeSum([-1,0,1,2,-1,-4]))