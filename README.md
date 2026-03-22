# leetcode
codes for leetcode exercises

## Python 小口诀
### Python Loop
- 只看元素，用 for x in xs
- 既看位置又看元素，用 enumerate
- 真要按位置操作，再用 range(len(xs))

### 字符串拼接
- 多次收集字符，用 list.append()
- 最后生成字符串，用 ''.join(list)

### 倒序
```
# 得到倒序后的新列表
nums = [1, 2, 3, 4]
print(nums[::-1])
```
```
# 反转字符串
chars = ["a", "b", "c"]
print("".join(reversed(chars)))
```

reverse()、reversed()、[::-1] 这三个别混了。

- list.reverse()
列表方法
原地修改
返回 None
nums = [1, 2, 3]
nums.reverse()
print(nums)   # [3, 2, 1]

- reversed(nums)
返回反向迭代器
不原地改

- nums[::-1]
返回新列表
不原地改



## Data Structures

### Heap 
- Priority Queue
- A complete binary tree
- Value of each node must be no greater than (or no less than) the value of its child nodes
- Time Complexity
    - insertion: O(logN)
    - deletion: O(logN)
    - finding minimun/maximum: O(1)
- can be used to implement priority queue


### Graph
- Disjoint Set
- find()
- union()
- union by rank
