

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # digits = [1, 2, 3]
        # [3, 2, 1]
        length = len(digits)

        number = 0
        # i = 0, 1, 2,  
        for i, digit in enumerate(digits):
            number += digit * pow(10, length - i - 1)
        
        number += 1

        plusOne = [int(digit) for digit in str(number)]

        return plusOne
        # slice the number
    
solution = Solution()
print(solution.plusOne([9]))
