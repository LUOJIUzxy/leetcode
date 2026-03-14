十、遍历 dict
1. 遍历 key
d = {"a": 1, "b": 2, "c": 3}

for key in d:
    print(key)

这和：

for key in d.keys():
    print(key)

效果基本一样。

2. 遍历 value
for value in d.values():
    print(value)
3. 同时遍历 key 和 value

这个最常用：

for key, value in d.items():
    print(key, value)

十一、判断 key 是否存在
d = {"a": 1, "b": 2}

print("a" in d)   # True
print("c" in d)   # False

注意这里判断的是 key，不是 value。

1 in d

这个不是看 value 里有没有 1，而是看 key 里有没有 1。

如果要判断 value 里有没有：

1 in d.values()

1. 计数

这个是最经典的。

s = "aabccc"
count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print(count)

结果：

{'a': 2, 'b': 1, 'c': 3}
2. 记录映射关系

比如学号到姓名：

students = {
    1001: "Alice",
    1002: "Bob"
}
3. 缓存 / memoization

把计算过的结果存起来，避免重复算。

memo = {}

这个在动态规划、递归里很常见。

4. 分组

比如按首字母分组：

words = ["apple", "ant", "banana", "book"]
groups = {}

for w in words:
    first = w[0]
    if first not in groups:
        groups[first] = []
    groups[first].append(w)

print(groups)

结果：

{'a': ['apple', 'ant'], 'b': ['banana', 'book']}
十三、刷题里最常见的三种 dict 写法
写法 1：普通计数
count = {}
for x in nums:
    count[x] = count.get(x, 0) + 1

这个非常经典。

写法 2：记录第一次出现的位置
first_index = {}
for i, x in enumerate(nums):
    if x not in first_index:
        first_index[x] = i
写法 3：key 对应列表
groups = {}
for x in nums:
    k = x % 3
    groups.setdefault(k, []).append(x)
十四、get 为什么好用

看这段计数代码：

count = {}
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

可以简化成：

count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1

因为：

如果 ch 存在，取原值

不存在，就默认 0

所以 get 在“计数”和“累加”里极其常见。

十五、setdefault 是什么

setdefault(key, default) 的意思是：

如果 key 在字典里，返回它的 value

如果不在，就先插入 key: default，再返回 default

比如：

d = {}
d.setdefault("a", []).append(1)
d.setdefault("a", []).append(2)
print(d)

结果：

{'a': [1, 2]}

这很适合做分组。

十六、字典推导式

像 list comprehension 一样，dict 也有推导式。

d = {x: x * x for x in range(5)}
print(d)

结果：

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

这在构造映射时很好用。

十七、dict 和 set 的关系

这个你一定要打通。

set
s = {1, 2, 3}

本质像是在存：

key = 1

key = 2

key = 3

只是没有 value。

dict
d = {"a": 1, "b": 2}

是在存：

"a" -> 1

"b" -> 2

所以可以粗暴理解为：

set 就是只有 key 的 dict

虽然底层实现细节不完全一样，但理解层面非常接近。

十八、常见坑
1. 访问不存在的 key
d["missing"]

会直接 KeyError。

更稳妥用：

d.get("missing")
2. 以为 in 判断的是 value
d = {"a": 1, "b": 2}
print(1 in d)   # False

因为 in 判断的是 key。

3. 字典遍历时乱改结构

比如：

for k in d:
    if some_condition:
        del d[k]

这可能报错，因为遍历过程中修改了字典结构。

稳妥做法通常是先复制 key：

for k in list(d.keys()):
    if some_condition:
        del d[k]
4. 可变对象做 key
d[[1, 2]] = "x"

不行，因为 list 不可哈希。

十九、复杂度

平均情况下：

查找 d[key]：O(1)

插入 d[key] = value：O(1)

删除：O(1)

最坏情况下理论上可能退化，但正常就按平均 O(1) 理解。

二十、和 list 对比
list 更适合

保持顺序

按位置访问

存一串同类元素

dict 更适合

按名字 / key 访问

建立映射关系

做计数 / 分组 / 缓存

比如：

["Alice", 20, "Munich"]

你得记住第几个位置是什么，容易乱。

而：

{"name": "Alice", "age": 20, "city": "Munich"}

就清楚得多。

二十一、面试里怎么讲 dict

可以这样说：

Python 的 dict 是基于哈希表实现的键值映射结构。
它通过 key 的哈希值快速定位存储位置，因此查找、插入、删除平均复杂度都是 O(1)。
字典的 key 必须是可哈希的不可变对象，而 value 没有限制。
dict 非常适合做映射、计数、分组、缓存等场景。

这段已经挺标准了。

二十二、几个经典刷题例子
1. Two Sum
def twoSum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i

这里 dict 存的是：

数值 -> 下标

这就是典型映射。

2. 统计频率
def count_chars(s):
    d = {}
    for ch in s:
        d[ch] = d.get(ch, 0) + 1
    return d
3. 分组异位词
def group_words(words):
    groups = {}
    for w in words:
        key = ''.join(sorted(w))
        groups.setdefault(key, []).append(w)
    return list(groups.values())
二十三、你现在可以这样理解三兄弟
list

像一排抽屉，按位置编号取

set

像一堆不重复的 key，只关心有没有

dict

像通讯录，名字对应电话号码

这个模型特别适合建立直觉。

二十四、最浓缩的结论

你把 dict 记成这四句就够了：

1. dict 是 key-value 映射

2. 底层是哈希表

3. key 必须可哈希，value 随意

4. 查找、插入、删除平均 O(1)

接下来最适合继续讲的是一个很关键的话题：

为什么 Python 里重写 __eq__ 往往也要重写 __hash__
这个一旦懂了，你对 set 和 dict 的底层逻辑就真的通了。