class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for astr in asteroids:
            if not stk:
                stk.append(astr)

            else:
                exploded = False
                while exploded == False and stk:
                    if (stk[-1] > 0 and astr < 0):
                        if abs(stk[-1]) > abs(astr):
                            exploded = True
                            break
                        elif abs(stk[-1]) == abs(astr):
                            stk.pop()
                            exploded = True
                        else:
                            stk.pop()
                    else:
                        break

                if not exploded:
                    stk.append(astr)

        return stk
