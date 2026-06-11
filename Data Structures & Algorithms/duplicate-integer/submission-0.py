class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contents = set()

        for num in nums:
            if num in contents:
                return True
            contents.add(num)

        return False