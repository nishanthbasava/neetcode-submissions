class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #here is a solution without division
        #three passes, one past for left side and one pass for right side, one for saving
        left = [1]
        left_val = 1
        length = len(nums)

        for num in nums:
            left_val *= num
            left.append(left_val)

        product = left[length - 1]
        right = [1] * length
        right_val = 1

        for i in range(length - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        output = []

        for i in range(length):
            output.append(left[i] * right[i])
            print("num: " + str(nums[i]))
            print("left: " + str(left[i]))
            print("right: " + str(right[i]))

        print(left)
        print(right)
        return output

        #below is a solution using division
        '''
        product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                product *= num
            else: 
                zeros += 1

        output = []

        if zeros > 1:
            for num in nums:
                output.append(0)

        elif zeros == 1:
            for num in nums:
                if num != 0:
                    output.append(0)
                else:
                    output.append(product)
    
        else: 
            for num in nums:
                output.append(int(product/num))

        return output

        '''

        