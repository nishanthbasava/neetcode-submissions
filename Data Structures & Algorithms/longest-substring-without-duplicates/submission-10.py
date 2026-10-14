class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        
        left, right = 0, 0

        while right <= len(s) - 1:
            if s[right] in seen:
                longest = max(longest, right - left)
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1

            seen.add(s[right])
            right += 1

        return max(longest, right - left)

        # Runtime: O(n)
        # Space: O(m), where m is unique characters in string
