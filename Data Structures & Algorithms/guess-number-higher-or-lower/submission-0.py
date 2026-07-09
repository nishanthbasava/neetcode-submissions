# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        p1 = 1
        p2 = n
        
        while True: 
            p3 = (p1 + p2) // 2
            if guess(p3) == 0:
                return p3
            elif guess(p3) == 1:
                p1 = p3 + 1
            else:
                p2 = p3 - 1
        