class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for string in strs:
            output += str(len(string)) + "#" + string

        return output

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        j = 0 

        while j != len(s) - 1: 
            while j < len(s) - 1 and s[j] != '#':
                j += 1

            if i == j:
                break
            
            length = int(s[i:j])

            i = j + 1
            new = ""
            for i in range (i, i + length):
                new+=s[i]

            output.append(new)

            j += length + 1
            i = j
        
        return output