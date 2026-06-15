class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        cur = ""

        while True:
            for word in strs:
                if i >= len(word):
                    return prefix

            cur = strs[0][i]

            for word in strs:
                if word[i] != cur:
                    return prefix

            prefix += cur
            i += 1