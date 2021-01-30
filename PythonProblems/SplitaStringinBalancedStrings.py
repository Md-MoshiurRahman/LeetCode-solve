class Solution(object):
    def balancedStringSplit(self, s):
        count = 0
        balance = 0

        for each in s:
            if each == 'L':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                count += 1

        return count

print(Solution().balancedStringSplit("RLRRLLRLRL"))
