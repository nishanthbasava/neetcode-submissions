class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        #to solve this problem, keep checking if valid palindrome until you reach an element that 
        #isn't valid. when you reach it, then check if left OR right is valid. if both not valid, then return False. otherwise return True
        #if every element equal, then it itself is a palindrome, so return True.
        
        def is_Palindrome(left, right):
            while (left < right): 
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1

        while (left < right):
            if s[left] != s[right]:
                return is_Palindrome(left, right - 1) or is_Palindrome(left + 1, right)
            
            left += 1
            right -= 1

        return True