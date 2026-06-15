class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        done = False
        i = 0
        cur = ""

        while not done:
            try: 
                prefix += cur
                cur = strs[0][i]
                for word in strs:
                    if word[i] != cur:
                        done = True
                        break
                i += 1
            except Exception as e:
                break

        return prefix