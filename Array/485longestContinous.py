
def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxNum = [0]
    lastValue = nums[0]
    currentMax = 1

    if len(nums) == 1:
        return 0

    for i, currentValue in enumerate(nums):
        #print(lastValue)
        
        if lastValue == nums[i]:
            if i != 0:
                currentMax += 1
            if i == len(nums) - 1:
                maxNum.append(currentMax)
            # else:
            #     currentMax
        else:
            maxNum.append(currentMax)
            currentMax = 1
            maxNum.append(1)


        lastValue = nums[i]

    return  max(maxNum)

print(findMaxConsecutiveOnes([0]))