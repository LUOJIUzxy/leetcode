
nums = list(map(int, input().split()))
n = nums[0]
x = nums[1]
y = nums[2]

gems = list(map(int, input().split()))

if len(gems) != n:
    # error
    print()

# 排列组合
# Cnx
# C = 3+2+1, C4/2 = 6

def dfs(start, picked, product):
#     nonlocal count
    # at most pick 2
    if picked == x:
        if product >= y:
            count += 1
            
        return count

    if  n - start < x - picked:
        return

    for i in range(start, n):
      count += dfs(i + 1, picked + 1, product * gems[i])

print(dfs(0, 0, 1))
    
