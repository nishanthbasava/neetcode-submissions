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

        for time in times:
            if not stk or time > stk[-1]:
                stk.append(time)

        return len(stk)