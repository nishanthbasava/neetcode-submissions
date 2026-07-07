class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(m), m is # of unique chars in string
        
        # Dynamic Sliding Window Problem

        max_length = 0
        left = 0
        seen = set()

        if len(s) == 1:
            return 1
        
        for right in range(len(s)):
            if s[right] in seen:
                max_length = max(max_length, right - left) #excluding one side
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else: 
                seen.add(s[right])
        
        return max(max_length, len(s) - left)
                