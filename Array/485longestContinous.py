# Find the ones
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxNum = []
    currentMax = 0

    for i, currentValue in enumerate(nums):
        if currentValue == 0:
            maxNum.append(currentMax)
            currentMax = 0
        else:
            currentMax += 1

        if i == len(nums) - 1:
            maxNum.append(currentMax)

    print(maxNum)
    return  max(maxNum)

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))