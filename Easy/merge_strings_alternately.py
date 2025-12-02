#Problem Merge Strings Alternately
from itertools import zip_longest


class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = ""  #merged string
        i = 0
        while i < len(word1) and i < len(word2):
            m = m + word1[i]
            m = m + word2[i]
            i = i + 1

        m = m + word1[i:]
        m = m + word2[i:]

        return m

    def mergeAlternately_ziplock(self, word1: str, word2: str) -> str:
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

    


a = Solution()
print(a.mergeAlternately_ziplock('abc', 'pqr'))
print(a.mergeAlternately_ziplock('ab', 'pqrs'))

print(a.mergeAlternately('lmno', 'xyz'))
print(a.mergeAlternately('lmn', 'xyz'))
