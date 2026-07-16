class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        freq = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                freq[5] += 1
            elif bill == 10:
                if freq[5] < 1:
                    return False
                else:
                    freq[10] += 1
                    freq[5] -= 1
            else: #bill == 20
                if (freq[10] < 1 or freq[5] < 1):
                    if freq[5] < 3:
                        return False
                    else:
                        freq[5] -= 3
                        freq[20] += 1
                else:
                    freq[5] -= 1
                    freq[10] -= 1
                    freq[20] += 1

        return True
