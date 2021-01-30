class Solution(object):
    def firstUniqChar(self, s):
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for key, value in hash_map.items():
            if value == 1:
                return s.index(key)
        return -1



print(Solution().firstUniqChar("dddccdbba"))
