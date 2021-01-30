class Solution(object):
    def reverse(self, x):
        negative = False

        if x<0:
            negative = True

        val = abs(x)

        sum = 0
        while(val > 0):
            temp = val%10
            sum = 10*sum + temp
            val = val //10

        maxvalue = pow(2,31) - 1

        if negative:
            if sum > maxvalue:
                return 0
            else:
                return -1*sum
        else:
            if sum > maxvalue:
                return 0
            else:
                return sum


s = Solution()

print(s.reverse(-123))