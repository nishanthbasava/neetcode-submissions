from bisect import bisect_left, bisect_right

def bs_with_package(arr, val):
    print(f"First index >= target: {bisect_left(arr, val)}")
    print(f"First index > target: {bisect_right(arr, val)}")

def bs_wo_package(arr, val):
    def bisect_left_mine(arr, val):
        p1 = 0 
        p2 = len(arr)

        while p2 > p1:
            mid = (p1 + p2) // 2

            if arr[mid] >= val:
                p2 = mid
            else:
                p1 = mid + 1
        
        return p1

    def bisect_right_mine(arr, val):
        p1 = 0
        p2 = len(arr)

        while p2 > p1:
            mid = (p1 + p2) // 2

            if arr[mid] > val:
                p2 = mid
            else:
                p1 = mid + 1

        return p1

    print(f"First index >= target (my version): {bisect_left_mine(arr, val)}")
    print(f"First index > target (my version): {bisect_right_mine(arr, val)}")

arr = [1, 4, 5, 6, 6, 7, 8, 9, 9, 9]
val = 4

bs_with_package(arr, val)
bs_wo_package(arr, val)
