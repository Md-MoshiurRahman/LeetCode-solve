class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        ln = len(nums)
        if ln%2 == 0:
            ans = (nums[int(ln/2) - 1] + nums[int(ln/2)])/2
            return ans
        else:
            ans = nums[int((ln-1)/2)]
            return ans



print(Solution().findMedianSortedArrays([2],[1,3]))
