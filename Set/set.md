模式 1：快速判断存在性
s = set(nums)
if target in s:
    ...
模式 2：去重后处理
s = set(nums)
for x in s:
    ...

模式 3：记录访问过
seen = set()
for x in nums:
    if x in seen:
        ...
    seen.add(x)

模式 4：从集合起点出发

这就是你上一题 longest consecutive sequence：

s = set(nums)
for x in s:
    if x - 1 not in s:
        # x 是起点

十九、常见坑

1. {} 不是空集合

错：

s = {}

这是 dict。

对：

s = set()
2. set 无序，不能索引

错：

s = {1, 2, 3}
print(s[0])
3. 不能放 list/dict/set

错：

s = {[1, 2], [3, 4]}
4. 一边遍历一边修改 set

比如：

s = {1, 2, 3}
for x in s:
    if x == 2:
        s.remove(x)

这种容易报错：

Set changed size during iteration

因为你在遍历的同时修改了集合结构。

如果真要改，通常先复制一份：

for x in s.copy():
    if x == 2:
        s.remove(x)

二十、set 和 frozenset

Python 还有个东西叫 frozenset，就是不可变集合。

fs = frozenset([1, 2, 3])

它和 set 类似，但不能 add/remove。

因为不可变，所以它本身可以作为别的 set 的元素，或者作为 dict 的 key。

普通 set 不行。

二十一、复杂度总结

常见操作平均复杂度：

x in s：O(1)

add：O(1)

remove/discard：O(1)

注意我说的是平均。
极端哈希冲突时会变差，但面试和刷题里默认按平均复杂度理解就行。

二十二、一个很标准的面试回答版本

如果面试官问你 Python set 是什么，你可以这样说：

Python 的 set 是基于哈希表实现的无序去重容器。
它的元素不能重复，并且元素必须是可哈希的不可变对象。
set 最重要的优势是成员查询平均复杂度为 O(1)，所以特别适合做去重、快速存在性判断、记录 visited 状态，以及集合运算，比如交集、并集、差集。
代价是它不保序，也不支持下标访问。

Python 的 set 底层基于哈希表实现。
插入、查找、删除时，先对元素计算哈希值，再根据哈希值定位到哈希表中的槽位。
若发生哈希冲突，会通过开放寻址等探测方式寻找合适位置。
set 通过“哈希值 + 相等性比较”来判断元素是否重复，因此元素必须是可哈希且哈希值稳定的对象。
这使得 set 的成员查询、插入和删除在平均情况下都能达到 O(1) 时间复杂度。


二十三、结合你那道题再看一眼

在 longest consecutive sequence 里：

num_set = set(nums)

这一句做了两件事：

去重

让 x in num_set 变成 O(1)

然后：

if num - 1 not in num_set:

这句是在找“连续序列的起点”。

然后：

while current + 1 in num_set:

这句是在不断往后扩展。

整题成立的基础，就是 set 的快速查找能力。

二十四、给你几个小例子加深感觉
例子 1：判断有无重复
nums = [1, 2, 3, 2]
print(len(nums) != len(set(nums)))

结果 True，说明有重复。

例子 2：找两个数组公共元素
a = [1, 2, 2, 3]
b = [2, 3, 4]

print(list(set(a) & set(b)))

结果：

[2, 3]
例子 3：只保留第一次见到的元素

这个不能直接用 set，因为 set 不保序。

你得这么写：

nums = [1, 2, 2, 3, 1, 4]
seen = set()
result = []

for x in nums:
    if x not in seen:
        seen.add(x)
        result.append(x)

print(result)

结果：

[1, 2, 3, 4]

这个是面试里很常见的写法。

二十五、你可以把 set 粗暴记成一句话

set = 不重复 + 查找快

看到下面这些关键词，就该想到它：

- 去重

- 判断是否存在

- 出现过没有

- 交集并集差集

- visited


十二、set 和 dict 的关系非常近

Python 里的 set 和 dict 底层思想非常像，都是哈希表。

你甚至可以粗暴理解成：

dict = 哈希表存 key -> value

set = 只存 key，不存 value

所以很多行为很像：

key / 元素 都必须可哈希

查找都快

本质都靠哈希表

这也是为什么你学懂 set，再学 dict 会轻松很多。

