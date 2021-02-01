class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        result = []
        mp = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] in mp:
                    mp[nums[i] + nums[j]].append([i,j])
                else:
                    mp[nums[i] + nums[j]] = [[i, j]]


        for i in range(n - 1):
            for j in range(i + 1, n):
                summ = nums[i] + nums[j]
                if (target - summ) in mp:
                    pairs = mp[target - summ]
                    for p in pairs:
                        if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
                            value = sorted([nums[i], nums[j], nums[p[0]], nums[p[1]]])
                            if value not in result:
                                result.append(value)

        return result



print(Solution().fourSum([-4,-3,-2,-1,0,0,1,2,3,4],0))