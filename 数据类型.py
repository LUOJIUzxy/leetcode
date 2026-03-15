
s = [] # list
s = set() # set
s = {} # dict


s = [0 ,1, 2, 3, 4] # list
s = {0, 1, 2, 3, 4} # set
s = {0: 'a', 1: 'b', 2: 'c'} # dict

# Python 的 set 底层基于哈希表实现。
# 插入、查找、删除时，先对元素计算哈希值，再根据哈希值定位到哈希表中的槽位。
# 若发生哈希冲突，会通过开放寻址等探测方式寻找合适位置。
# set 通过“哈希值 + 相等性比较”来判断元素是否重复，因此元素必须是可哈希且哈希值稳定的对象。
# 这使得 set 的成员查询、插入和删除在平均情况下都能达到 O(1) 时间复杂度。


# Python 的 dict 是基于哈希表实现的键值映射结构。
# 它通过 key 的哈希值快速定位存储位置，因此查找、插入、删除平均复杂度都是 O(1)。
# 字典的 key 必须是可哈希的不可变对象，而 value 没有限制。
# dict 非常适合做映射、计数、分组、缓存等场景。

a = ()      # 空 tuple
b = (1, 2)  # tuple
c = (1)     # 不是 tuple，是 int
d = (1,)    # 单元素 tuple

[x for x in range(3)]      # list
(x for x in range(3))      # generator，不是 tuple
{x for x in range(3)}      # set
{x: x*x for x in range(3)} # dict
tuple(x for x in range(3))

3 in [1, 2, 3]         # 查元素
3 in {1, 2, 3}         # 查元素
"a" in {"a": 1, "b": 2} # 查 key，不查 value