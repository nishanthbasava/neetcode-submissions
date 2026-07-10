class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)

        pairs = list(zip(position, speed))
        pairs.sort(key = lambda x : x[0], reverse=True)

        times = [0] * len(position)
        for i in range(len(position)):
            times[i] = (target - pairs[i][0]) / pairs[i][1]

        stk = []
        count = 0

        for time in times:
            while stk and time > stk[-1]:
                stk.pop()

                if not stk:
                    count += 1

            stk.append(time)

        if stk:
            return count + 1
        return count