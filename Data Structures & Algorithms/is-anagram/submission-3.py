class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_to_freq_s = {}
        char_to_freq_t = {}

        for character in s:
            if character not in char_to_freq_s:
                char_to_freq_s[character] = 1
            else:
                char_to_freq_s[character] += 1

        for character in t:
            if character not in char_to_freq_t:
                char_to_freq_t[character] = 1
            else:
                char_to_freq_t[character] += 1

        if char_to_freq_s == char_to_freq_t:
            return True
        return False