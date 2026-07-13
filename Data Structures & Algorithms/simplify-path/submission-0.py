class Solution:
    def simplifyPath(self, path: str) -> str:
        # Time Complexity: O(n)
        # Space Complexity: O(n)

        print(path.split("/"))
        stk = []

        for component in path.split("/"):
            if component == "" or component == ".":
                continue
            elif component == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(component)

        return "/" + "/".join(stk)