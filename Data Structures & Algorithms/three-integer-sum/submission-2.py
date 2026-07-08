class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        def twoSum(arr: List[int], target: int) -> List[List[int]]:
            p1 = 0 
            p2 = len(arr) - 1
            pairs = []

            while p1 < p2:
                if arr[p1] + arr[p2] == target:
                    pairs.append([arr[p1], arr[p2]])
                    p1 += 1
                    p2 -= 1

                    while p1 < p2 and arr[p1] == arr[p1 - 1]:
                        p1 += 1
                    while p1 < p2 and arr[p2] == arr[p2 + 1]:
                        p2 -= 1
                        
                elif arr[p1] + arr[p2] > target:
                    p2 -= 1
                else:
                    p1 += 1
            
            return pairs

        for p3 in range(len(nums)):
            if p3 > 0 and nums[p3] == nums[p3 - 1]:
                continue

            triplets = twoSum(nums[p3 + 1:], 0 - nums[p3])
            if triplets != []:
                for triplet in triplets:
                    output.append([nums[p3]] + triplet)

        return output