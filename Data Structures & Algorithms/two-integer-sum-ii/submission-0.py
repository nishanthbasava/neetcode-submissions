class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        output = []

        p1 = 0
        p2 = len(numbers) - 1

        while True:
            if numbers[p1] + numbers[p2] == target:
                output.append(p1 + 1)
                output.append(p2 + 1)
                break
            elif numbers[p1] + numbers[p2] < target:
                p1 += 1
            else: #sum is greater
                p2 -= 1

        return output