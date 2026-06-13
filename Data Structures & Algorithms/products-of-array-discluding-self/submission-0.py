class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #really fast edge case, if you find 0, then every other element in output is 0

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


        