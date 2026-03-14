# This code removes duplicates from a list 
# while preserving the order of the first occurrence.

nums = [1, 2, 2, 3, 1, 4]
seen = set()
result = []

for x in nums:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)

# This code checks if there are duplicates in the list by comparing the length of the list with the length of a set created from the list.
nums = [1, 2, 3, 2]
print(len(nums) != len(set(nums)))