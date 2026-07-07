class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(1)

        people.sort()

        p1 = 0 
        p2 = len(people) - 1
        count = 0

        while p1 <= p2:
            if people[p1] + people[p2] > limit:
                count += 1
                p2 -= 1
            else:
                count += 1
                p1 += 1
                p2 -= 1

        return count