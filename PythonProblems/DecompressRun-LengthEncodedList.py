class Solution(object):
    def decompressRLElist(self, nums):
        decompressNums = []
        freq = []
        value = []
        i = 0
        while i<len(nums):
            freq.append(nums[i])
            value.append(nums[i+1])
            i += 2
        for j in range(len(freq)):
            for k in range(freq[j]):
                decompressNums.append(value[j])

        return decompressNums

print(Solution().decompressRLElist([1,1,2,3]))