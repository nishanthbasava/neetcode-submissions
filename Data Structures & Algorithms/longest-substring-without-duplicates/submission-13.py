class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        length = 0
        p1 = 0

        for i, char in enumerate(s):
            if char not in seen:
                seen.add(char)
                length += 1

            else:
                longest = max(longest, length)
                while char in seen:
                    seen.remove(s[p1])
                    p1 += 1

                length = i - p1 + 1
                seen.add(char)

        return max(longest, length)

