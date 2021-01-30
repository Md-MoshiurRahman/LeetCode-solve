class Solution(object):
    def func(self, string):
        min_char = min(string)
        return string.count(min_char)

    def numSmallerByFrequency(self, queries, words):
        for i in range(len(words)):
            words[i] = self.func(words[i])

        for j in range(len(queries)):
            f_q = self.func(queries[j])
            count = 0
            for i in range(len(words)):
                if f_q < words[i]:
                    count += 1
            queries[j] = count

        return queries

print(Solution().numSmallerByFrequency(["bbb","cc"],["a","aa","aaa","aaaa"]))
