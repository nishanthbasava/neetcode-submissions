class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        freq_anagrams = []

        for word in strs:
            added = False
            freq_word = {}

            for char in word:
                if char in freq_word:
                    freq_word[char] = freq_word[char] + 1
                else:
                    freq_word[char] = 1

            i=0
            for anagram in output:
                if freq_anagrams[i] == freq_word:
                    anagram.append(word)
                    added = True
                    break
                i += 1

            if added == False:
                output.append([word])
                freq_anagrams.append(freq_word)
                
        return output