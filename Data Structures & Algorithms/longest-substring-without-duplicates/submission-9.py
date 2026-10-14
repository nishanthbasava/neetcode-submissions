class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        
        p0, p1 = 0, 0

        if len(s) == 1:
            return 1

        while p1 <= len(s) - 1:
            if s[p1] in seen:
                longest = max(longest, p1 - p0)
                while s[p1] in seen:
                    seen.remove(s[p0])
                    p0 += 1

            seen.add(s[p1])
            p1 += 1

        return max(longest, p1 - p0)

