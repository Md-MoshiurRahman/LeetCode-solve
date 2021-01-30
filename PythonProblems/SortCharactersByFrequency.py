import operator
class Solution(object):
    def frequencySort(self, s):
        hash_map = {}
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1


        finalS = ""
        sorted_hashmap = sorted(hash_map.items(), key=operator.itemgetter(1))
        sorted_hashmap.reverse()

        for i in sorted_hashmap:
            key, value = i
            finalS += str(key) * value
        return finalS



print(Solution().frequencySort("tree"))
