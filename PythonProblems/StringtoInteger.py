class Solution(object):
    def myAtoi(self, str):
        str = str.strip()
        n = len(str)

        if n == 0:
            return 0

        if (str[0] >= '0' and str[0] <= '9') or str[0]=='-' or str[0]=='+':
            sum = 0
            if (str[0] == '-'):
                if n == 1:
                    return 0
                i = 1
                while (str[i] >= '0' and str[i] <= '9'):
                    sum = sum * 10 + int(str[i])

                    if i == n - 1:
                        break
                    else:
                        i += 1

                if sum > pow(2,31):
                    return -1*pow(2,31)
                else:
                    return -1 * sum

            elif (str[0] == '+'):
                if n == 1:
                    return 0
                i = 1
                while (str[i] >= '0' and str[i] <= '9'):
                    sum = sum * 10 + int(str[i])

                    if i == n - 1:
                        break
                    else:
                        i += 1

                if sum > pow(2, 31)-1:
                    return (pow(2, 31) -1)
                else:
                    return sum


            else:
                i = 0
                while (str[i] >= '0' and str[i] <= '9'):
                    sum = sum * 10 + int(str[i])

                    if i == n - 1:
                        break
                    else:
                        i += 1

                if sum > pow(2, 31) - 1:
                    return (pow(2, 31) - 1)
                else:
                    return sum
        else:
            return 0



print(Solution().myAtoi("-91283472332"))