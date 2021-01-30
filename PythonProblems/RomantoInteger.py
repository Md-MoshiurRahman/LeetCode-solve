class Solution(object):
    def romanToInt(self, str):
        hash_map = {}
        hash_map['I'] = 1
        hash_map['V'] = 5
        hash_map['X'] = 10
        hash_map['L'] = 50
        hash_map['C'] = 100
        hash_map['D'] = 500
        hash_map['M'] = 1000

        length = len(str)
        i = 0
        num = 0
        while i < length:
            if length-i >= 2:
                if str[i]=='I' and str[i+1]=='V':
                    num += 4
                    i += 2
                elif str[i]=='I' and str[i+1]=='X':
                    num += 9
                    i += 2

                elif str[i] == 'X' and str[i + 1] == 'L':
                    num += 40
                    i += 2
                elif str[i] == 'X' and str[i + 1] == 'C':
                    num += 90
                    i += 2

                elif str[i]=='C' and str[i+1]=='D':
                    num += 400
                    i += 2
                elif str[i]=='C' and str[i+1]=='M':
                    num += 900
                    i += 2

                else:
                    num += hash_map[str[i]]
                    i += 1
            else:
                num += hash_map[str[i]]
                i += 1

        return num


print(Solution().romanToInt("MCMXCIV"))