





################time limit exceed###########





class Solution(object):
    def findDiagonalOrder(self, nums):
        diagonal = []
        total = 0
        length = len(nums)
        arrlen = []
        for i in range(len(nums)):
            x = len(nums[i])
            total += x
            arrlen.append(x)
        count = 0
        i = 0
        k = 0
        j = 0
        while(True):
            if i >= len(nums):
                k = len(nums)-1
                j = i-(len(nums)-1)
            else:
                k = i
                j = 0
            while j<i+1:
                if j<len(nums[k]):
                    diagonal.append(nums[k][j])
                    count += 1
                    if count == total:
                        return diagonal
                k-=1
                j+=1
            i += 1


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))